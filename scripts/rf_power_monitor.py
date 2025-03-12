#! /usr/bin/python
# Copyright Notice:
# Copyright 2019-2025 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Tacklebox/blob/main/LICENSE.md

"""
Redfish Power Monitor

File : rf_power_monitor.py

Brief : This script uses the redfish_utilities module to monitor power
"""

import argparse
from redfish_utilities.arguments import create_parent_parser, validate_args
from redfish_utilities.logger import setup_logger

description = "A tool to collect power data from a Redfish service"
parent_parser = create_parent_parser(description=description, auth=True, rhost=True)
argget = argparse.ArgumentParser(parents=[parent_parser])

args = argget.parse_args()
validate_args(args)
logger = setup_logger(
    file_log=args.log_to_file, stream_log=args.log_to_console, log_level=args.log_level, file_name=__file__
)

print("Power monitor")