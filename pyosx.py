#!/usr/bin/env python
import argparse
from functions import *

# Confirm that the system is running OS X
confirm_osx()

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('type', type=str, help='Type of results to display: full, system, uuids, clocks, cpu, ram')
args = parser.parse_args()

# Print results
print_results(args.type)