#!/usr/bin/env python
from functions import *
import unittest2 as unittest

# Testing on TJW-iMac
# Testing will fail on any other hardware

class CpuTest(unittest.TestCase):
    """
    Tests the get_cpu_information function
    """

    def test_cpu_physical_cores_value(self):
        """
        Tests the get_cpu_information function for cpu_physical_cores
        """
        
        cpu_architecture, cpu_model, cpu_physical_cores, cpu_logical_cores = get_cpu_information()
        
        # Check to make sure the number of physical cores is 4
        self.assertEqual(cpu_physical_cores, 4)
    
    def test_cpu_physical_cores_type(self):
        """
        Tests the get_cpu_information function for cpu_physical_cores
        """
        
        cpu_architecture, cpu_model, cpu_physical_cores, cpu_logical_cores = get_cpu_information()
        
        # Check to make sure the returned value is an int
        self.assertEqual(type(cpu_physical_cores), int)
        
if __name__ == '__main__':
    unittest.main()