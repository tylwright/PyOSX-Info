#!/usr/bin/env python
from functions import *
import unittest2 as unittest

# Testing on TJW-iMac
# Testing will fail on any other hardware

class VersionTest(unittest.TestCase):
    """
    Tests the get_osx_version function
    """
    
    def test_osx_version_number_type(self):
        """
        Tests the get_osx_version function for running_version_number
        """
        
        running_version_number = get_osx_version()[0]
        
        # Check to make sure the returned valued is a string
        self.assertEqual(type(running_version_number), str)
    
    def test_osx_version_number_value(self):
        """
        Tests the get_osx_version function for running_version_number
        """
        
        running_version_number = get_osx_version()[0]
        
        # Check to make sure the returned valued is 10.11.1
        self.assertEqual(running_version_number, '10.11.1')
        
    def test_osx_version_name_type(self):
        """
        Tests the get_osx_version function for running_version_name
        """
        
        running_version_name = get_osx_version()[1]
        
        # Check to make sure the returned valued is a string
        self.assertEqual(type(running_version_name), str)
    
    def test_osx_version_name_value(self):
        """
        Tests the get_osx_version function for running_version_name
        """
        
        running_version_name = get_osx_version()[1]
        
        # Check to make sure the returned valued is 10.11.1
        self.assertEqual(running_version_name, 'El Capitan')

class CPUTest(unittest.TestCase):
    """
    Tests the get_cpu_information function
    """

    def test_cpu_physical_cores_value(self):
        """
        Tests the get_cpu_information function for cpu_physical_cores
        """
        
        cpu_physical_cores = get_cpu_information()[2]
        
        # Check to make sure the number of physical cores is 4
        self.assertEqual(cpu_physical_cores, 4)
    
    def test_cpu_physical_cores_type(self):
        """
        Tests the get_cpu_information function for cpu_physical_cores
        """
        
        cpu_physical_cores = get_cpu_information()[2]
        
        # Check to make sure the returned value is an int
        self.assertEqual(type(cpu_physical_cores), int)
        
    def test_cpu_logical_cores_value(self):
        """
        Tests the get_cpu_information function for cpu_logical_cores
        """
        
        cpu_logical_cores = get_cpu_information()[3]
        
        # Check to make sure the number of logical cores is 8
        self.assertEqual(cpu_logical_cores, 8)
    
    def test_cpu_logical_cores_type(self):
        """
        Tests the get_cpu_information function for cpu_logical_cores
        """
        
        cpu_logical_cores = get_cpu_information()[3]
        
        # Check to make sure the returned value is an int
        self.assertEqual(type(cpu_logical_cores), int)
        
    def test_cpu_architecture_value(self):
        """
        Tests the get_cpu_information function for cpu_architecture
        """
        
        cpu_architecture = get_cpu_information()[0]
        
        # Check to make sure the returned value is "x86_64"
        self.assertEqual(cpu_architecture, 'x86_64')
        
    def test_cpu_architecture_type(self):
        """
        Tests the get_cpu_information function for cpu_architecture
        """
        
        cpu_architecture = get_cpu_information()[0]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(cpu_architecture), str)
        
    def test_cpu_model_value(self):
        """
        Tests the get_cpu_information function for cpu_model
        """
        
        cpu_model = get_cpu_information()[1]
        
        # Check to make sure the returned value is "Intel(R) Core(TM) i7-4771 CPU @ 3.50GHz"
        self.assertEqual(cpu_model, 'Intel(R) Core(TM) i7-4771 CPU @ 3.50GHz')
        
    def test_cpu_model_type(self):
        """
        Tests the get_cpu_information function for cpu_model
        """
        
        cpu_model = get_cpu_information()[1]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(cpu_model), str)
        
    def test_cpu_processor_count_value(self):
        """
        Tests the get_cpu_information function for cpu_processor_count
        """
        
        cpu_processor_count = get_cpu_information()[4]        
        
        # Check to make sure the returned value is "Intel(R) Core(TM) i7-4771 CPU @ 3.50GHz"
        self.assertEqual(cpu_processor_count, 1)
        
    def test_cpu_processor_count_type(self):
        """
        Tests the get_cpu_information function for cpu_processor_count
        """
        
        cpu_processor_count = get_cpu_information()[4]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(cpu_processor_count), int)
        
class RAMTest(unittest.TestCase):
    """
    Tests the get_ram_information function
    """

    def test_ram_total_value(self):
        """
        Tests the get_ram_information function for ram_total
        """
        
        ram_total = get_ram_information()[0]
        
        # Check to make sure the total amount of RAM is 32G
        self.assertEqual(ram_total, '32G')
    
    def test_ram_total_type(self):
        """
        Tests the get_ram_information function for ram_total
        """
        
        ram_total = get_ram_information()[0]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(ram_total), str)
        
    def test_swap_total_value(self):
        """
        Tests the get_ram_information function for swap_total
        """
        
        swap_total = get_ram_information()[1]
        
        # Check to make sure the total amount of swap is is something "G"
        self.assertIn('G', swap_total)
    
    def test_swap_total_type(self):
        """
        Tests the get_ram_information function for swap_total
        """
        
        swap_total = get_ram_information()[1]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(swap_total), str)
        
class HostnameTest(unittest.TestCase):
    """
    Tests the get_hostname function
    """
    
    def test_hostname_value(self):
        """
        Tests the get_hostname function
        """
        
        hostname = get_hostname()
        
        # Check to make sure the hostname is "tjw-imac.grid.labs"
        self.assertEqual(hostname, 'tjw-imac.grid.labs')
    
    def test_hostname_type(self):
        """
        Tests the get_hostname function
        """
        
        hostname = get_hostname()
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(hostname), str)
    
class UUIDTest(unittest.TestCase):
    """
    Tests the get_uuids function
    """
    
    def test_kernel_uuid_value(self):
        """
        Tests the get_uuid function for kernel_uuid
        """
        
        kernel_uuid = get_uuids()[0]
        
        # Check to make sure it contains "-"
        # Exact matching is not done on purpose - UUIDs should be kept private!
        self.assertIn("-", kernel_uuid)
        
    def test_kernel_uuid_type(self):
        """
        Tests the get_uuid function for kernel_uuid
        """
        
        kernel_uuid = get_uuids()[0]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(kernel_uuid), str)
        
    def test_hardware_uuid_value(self):
        """
        Tests the get_uuid function for hardware_uuid
        """
        
        hardware_uuid = get_uuids()[1]
        
        # Check to make sure it contains "-"
        # Exact matching is not done on purpose - UUIDs should be kept private!
        self.assertIn("-", hardware_uuid)
        
    def test_hardware_uuid_type(self):
        """
        Tests the get_uuid function for hardware_uuid
        """
        
        hardware_uuid = get_uuids()[1]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(hardware_uuid), str)
        
    def test_boot_session_uuid_value(self):
        """
        Tests the get_uuid function for boot_session_uuid
        """
        
        boot_session_uuid = get_uuids()[2]
        
        # Check to make sure it contains "-"
        # Exact matching is not done on purpose - UUIDs should be kept private!
        self.assertIn("-", boot_session_uuid)
        
    def test_hardware_uuid_type(self):
        """
        Tests the get_uuid function for boot_session_uuid
        """
        
        boot_session_uuid = get_uuids()[2]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(boot_session_uuid), str)
        
class ClocksTest(unittest.TestCase):
    """
    Tests the get_clocks function
    """
    
    def test_last_boot_value(self):
        """
        Tests the get_clocks function for last_boot
        """
        last_boot = get_clocks()
        
        # Check to make sure the returned value is not null
        self.assertIsNotNone(last_boot)
    
    def test_last_boot_type(self):
        """
        Tests the get_clocks function for last_boot
        """
        last_boot = get_clocks()
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(last_boot), str)
        
class SerialTest(unittest.TestCase):
    """
    Tests the get_serial function
    """
    
    def test_serial_value(self):
        """
        Tests the get_serial function
        """
        
        serial = get_serial()
        
        # Check to make sure it is not null
        # Exact matching is not done on purpose - serials should be kept private!
        self.assertIsNotNone(serial)
        
    def test_serial_type(self):
        """
        Tests the get_uuid function
        """
        
        serial = get_serial()
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(serial), str)
        
class ModelTest(unittest.TestCase):
    """
    Tests the get_model function
    """
    
    def test_model_name_value(self):
        """
        Tests the get_model function for model_name
        """
        
        model_name = get_model()[0]
        
        # Check to make sure the model_name is 'iMac'
        self.assertEqual(model_name, 'iMac')
        
    def test_model_name_type(self):
        """
        Tests the get_model function for model_name
        """
        
        model_name = get_model()[0]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(model_name), str)
        
    def test_model_identifier_value(self):
        """
        Tests the get_model function for model__identifier
        """
        
        model_identifier = get_model()[1]
        
        # Check to make sure the model_name is 'iMac14,2'
        self.assertEqual(model_identifier, 'iMac14,2')
        
    def test_model__identifier_type(self):
        """
        Tests the get_model function for model__identifier
        """
        
        model_identifier = get_model()[1]
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(model_identifier), str) 

class SMCTest(unittest.TestCase):
    """
    Tests the get_smc_version function
    """
    
    def test_smc_version_value(self):
        """
        Tests the get_smc_version function
        """
        
        smc_version = get_smc_version()
        
        # Check to make sure the smc_version is '2.15f7'
        self.assertEqual(smc_version, '2.15f7')
        
    def test_smc_version_type(self):
        """
        Tests the get_smc_version function
        """
        
        smc_version = get_smc_version()
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(smc_version), str)
        
class BootROMTest(unittest.TestCase):
    """
    Tests the get_boot_rom_version function
    """
    
    def test_boot_rom_version_value(self):
        """
        Tests the get_boot_rom_version function
        """
        
        boot_rom_version = get_boot_rom_version()
        
        # Check to make sure the boot_rom_version is 'IM142.0118.B12'
        self.assertEqual(boot_rom_version, 'IM142.0118.B12')
        
    def test_boot_rom_version_type(self):
        """
        Tests the get_boot_rom_version function
        """
        
        boot_rom_version = get_boot_rom_version()
        
        # Check to make sure the returned value is a string
        self.assertEqual(type(boot_rom_version), str)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)