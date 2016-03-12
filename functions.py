#!/usr/bin/env python
import os, sys, platform
from tabulate import tabulate
from hurry.filesize import size

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
        running_version[0] [string]: Version number (ex. 10.11.1)
    """
    
    # Get version
    running_version = platform.mac_ver()

    # Return version
    return running_version[0]
    
def get_cpu_information():
    """
    Detects information about the CPU
    Returns:
        cpu_architecture [string]: CPU architecture (ex. x86)
        cpu_model [string]: CPU model (ex. Intel Core i7 CPU @ 3.50GHz)
        cpu_physical_cores[int]: Number of physical cores
        cpu_logical_cores [int]: Number of logical cores
    """
    
    # Get CPU architecture
    cpu_architecture = platform.machine()
    
    # Get CPU model
    cpu_model = os.popen('sysctl -n machdep.cpu.brand_string').read().rstrip()
    
    # Get number of physical cores that the system has
    cpu_physical_cores = int(os.popen('sysctl hw.physicalcpu').read().rstrip().translate(None, 'hw.physicalcpu: '))
    
    # Get number of logical cores that the system has
    cpu_logical_cores = int(os.popen('sysctl hw.logicalcpu').read().rstrip().translate(None, 'hw.logicalcpu: '))
    
    # Return architecture
    return cpu_architecture, cpu_model, cpu_physical_cores, cpu_logical_cores
    
def get_ram_information():
    """
    Detects information about the RAM
    Returns:
        ram_total [string]: Total amount of RAM in human readable format
    """
    
    # Get total RAM (in human readable format)
    ram_total = size(int(os.popen('sysctl hw.memsize').read().rstrip().translate(None, 'hw.memsize: ')))
    
    return ram_total
  
def print_results(type):
    """
    Prints system information
    Parameters:
        type [string]:
            full: Print everything that is available
    """
    
    # Get OS X version number
    osx_version_number = get_osx_version()
    
    # Get CPU info
    cpu_architecture, cpu_model, cpu_physical_cores, cpu_logical_cores = get_cpu_information()
    
    # Get RAM info
    ram_total = get_ram_information()
    
    # Print results
    print "========================================"
    print "Mac OS X {}".format(osx_version_number)
    print "========================================"
    print "CPU Info:"
    cpu_table = [
        ["Model", cpu_model],
        ["Architecture", cpu_architecture],
        ["Physical Cores", cpu_physical_cores],
        ["Logical Cores", cpu_logical_cores]
    ]
    print tabulate(cpu_table, tablefmt="fancy_grid")
    print "\nRAM Info:"
    ram_table = [
        ["Total RAM:", ram_total]
    ]
    print tabulate(ram_table, tablefmt="fancy_grid")
    #print tabulate(cpu_table, tablefmt="html") # Future web interface?