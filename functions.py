#!/usr/bin/env python
import datetime, os, sys, platform
from tabulate import tabulate
from hurry.filesize import size, alternative

def confirm_osx():
    """
    Makes sure the system is running OS X
    """
    
    # Get platform
    running_platform = platform.system()

    # If OS Name is not OS X: alert the user, throw an exception, and exit
    if running_platform != "Darwin":
        sys.exit("Error: System is not running OS X")
        
def get_osx_version():
    """
    Detects which version of OS X the system is running
    Returns:
        running_version_number [string]: Version number (ex. 10.11.1)
        running_version_name [string]: Version name (ex. El Capitan)
    """
    
    # Get version number
    running_version_number = platform.mac_ver()
    running_version_number = running_version_number[0]
    
    if running_version_number.startswith('10.11'):
        running_version_name = "El Capitan"
    elif running_version_number.startswith('10.10'):
        running_version_name = "Yosemite"
    elif running_version_number.startswith('10.9'):
        running_version_name = "Mavericks"
    elif running_version_number.startswith('10.8'):
        running_version_name = "Mountain Lion"
    elif running_version_number.startswith('10.7'):
        running_version_name = "Lion"
    elif running_version_number.startswith('10.6'):
        running_version_name = "Snow Leopard"
    elif running_version_number.startswith('10.5'):
        running_version_name = "Leopard"
    elif running_version_number.startswith('10.4'):
        running_version_name = "Tiger"
    elif running_version_number.startswith('10.3'):
        running_version_name = "Panther"
    elif running_version_number.startswith('10.2'):
        running_version_name = "Jaguar"
    elif running_version_number.startswith('10.1'):
        running_version_name = "Puma"
    elif running_version_number.startswith('10.0'):
        running_version_name = "Cheetah"
    else:
        running_version_name = "Unknown"

    # Return version
    return running_version_number, running_version_name
    
def get_cpu_information():
    """
    Detects information about the CPU
    Returns:
        cpu_architecture [string]: CPU architecture (ex. x86)
        cpu_model [string]: CPU model (ex. Intel Core i7 CPU @ 3.50GHz)
        cpu_physical_cores[int]: Number of physical cores
        cpu_logical_cores [int]: Number of logical cores
        cpu_processor_count[int]: Number of processors installed
    """
    
    # Get CPU architecture
    cpu_architecture = platform.machine()
    
    # Get CPU model
    cpu_model = os.popen('sysctl -n machdep.cpu.brand_string').read().rstrip()
    
    # Get number of physical cores that the system has
    cpu_physical_cores = int(os.popen('sysctl hw.physicalcpu').read().rstrip().translate(None, 'hw.physicalcpu: '))
    
    # Get number of logical cores that the system has
    cpu_logical_cores = int(os.popen('sysctl hw.logicalcpu').read().rstrip().translate(None, 'hw.logicalcpu: '))
    
    # Get number of processors installed
    cpu_processor_count = int(os.popen('system_profiler SPHardwareDataType | grep "Number of Processors:"').read().rstrip().translate(None, 'Number of Processors: '))
    
    # Return CPU info
    return cpu_architecture, cpu_model, cpu_physical_cores, cpu_logical_cores, cpu_processor_count
    
def get_ram_information():
    """
    Detects information about the RAM
    Returns:
        ram_total [string]: Total amount of RAM in human readable format
        swap_total [string]: Total amount of swap available in human readable format
    """
    
    # Get total RAM (in human readable format)
    ram_total = size(int(os.popen('sysctl hw.memsize').read().rstrip().translate(None, 'hw.memsize: ')))
    
    # Get swap
    swap_total = os.popen('sysctl vm.swapusage').read().rstrip().replace('vm.swapusage: ', '')
    swap_total = swap_total.split('total = ')[1]
    swap_total = swap_total.split('  used =')[0]
    swap_total = swap_total.split('.')[0]
    swap_total = size(int(swap_total) * 1024 * 1024)
    
    # Return total RAM
    return ram_total, swap_total
    
def get_hostname():
    """
    Detects the system's hostname
    Returns:
        hostname [string]: System's hostname (ex. mac.company.com)
    """
    
    # Get hostname
    hostname = os.popen('sysctl kern.hostname').read().rstrip().replace('kern.hostname: ', '')
    
    # Return hostname
    return hostname
  
def get_uuids():
    """
    Detects the system's UUIDs
    Returns:
        kernel_uuid [string]: UUID of kernel
        hardware_uuid [string]: UUID of hardware
    """
    
    # Get UUID of kernel
    kernel_uuid = os.popen('sysctl kern.uuid').read().rstrip().translate(None, 'kern.uuid: ')
    
    # Get UUID of hardware
    hardware_uuid = os.popen('system_profiler SPHardwareDataType | grep "Hardware UUID:"').read().rstrip().translate(None, 'Hardware UUID: ')
    
    # Return UUID
    return kernel_uuid, hardware_uuid
    
def get_clocks():
    """
    Detects various clocks such as current time/date, last reboot, uptime, etc.
    Returns:
        last_boot [string]: Date when the system was last booted
    """
    
    # Get Uptime
    last_boot = os.popen('sysctl kern.boottime').read().rstrip()
    last_boot = last_boot.split(' } ')[1]
    
    # Return last boot
    return last_boot 
  
def get_serial():
    """
    Detects the serial number of the system
    Returns:
        serial [string]: Serial number of system
    """
    
    # Get serial number
    serial = os.popen('system_profiler SPHardwareDataType | grep "Serial Number"').read().rstrip().translate(None, 'Serial Number (system): ')
    
    # Return serial
    return serial
  
def get_model():
    """
    Detects the model of the system
    Returns:
        model_name [string]: Model name of system
        model_identifier [string]: Model identifier of system
    """
    
    # Get model name
    model_name = os.popen('system_profiler SPHardwareDataType | grep "Model Name:"').read().rstrip().replace('Model Name: ', '').replace(' ','')
    
    # Get model identifier
    model_identifier = os.popen('system_profiler SPHardwareDataType | grep "Model Identifier:"').read().rstrip().replace('Model Identifier: ', '').replace(' ','')
    
    # Return model info
    return model_name, model_identifier
  
def print_results(type):
    """
    Prints system information
    Parameters:
        type [string]:
            full: Print everything that is available
    """
    
    # Get OS X version info
    osx_version_number, osx_version_name = get_osx_version()
    
    # Get hostname
    hostname = get_hostname()
    
    # Get UUIDs
    kernel_uuid, hardware_uuid = get_uuids()
    
    # Get serial
    serial = get_serial()
    
    # Get model info
    model_name, model_identifier = get_model()
    
    # Get Clocks
    last_boot = get_clocks()
    
    # Get CPU info
    cpu_architecture, cpu_model, cpu_physical_cores, cpu_logical_cores, cpu_processor_count = get_cpu_information()
    
    # Get RAM info
    ram_total, swap_total = get_ram_information()
    
    # Print results
    print "\nSystem:"
    system_table = [
        ["OS X Version", "{} ({})".format(osx_version_number, osx_version_name)],
        ["Hostname", hostname],
        ["Model", "{} ({})".format(model_name, model_identifier)],
        ["Serial", serial],
    ]
    print tabulate(system_table, tablefmt="fancy_grid")
    print "\nUUIDs:"
    uuid_table = [
        ["Kernel UUID", kernel_uuid],
        ["Hardware UUID", hardware_uuid]
    ]
    print tabulate(uuid_table, tablefmt="fancy_grid")
    print "\nSystem Clocks:"
    clocks_table = [
        ["Last Boot", last_boot]
    ]
    print tabulate(clocks_table, tablefmt="fancy_grid")
    print "\nCPU Info:"
    cpu_table = [
        ["Model", cpu_model],
        ["Architecture", cpu_architecture],
        ["Total Processors", cpu_processor_count],
        ["Physical Cores", cpu_physical_cores],
        ["Logical Cores", cpu_logical_cores]
    ]
    print tabulate(cpu_table, tablefmt="fancy_grid")
    print "\nRAM Info:"
    ram_table = [
        ["Total RAM", ram_total],
        ["Total swap", swap_total]
    ]
    print tabulate(ram_table, tablefmt="fancy_grid")
    #print tabulate(cpu_table, tablefmt="html") # Future web interface?
    print ""