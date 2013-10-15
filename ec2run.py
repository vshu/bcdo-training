#!/usr/bin/env python
"""command line arguments are modeled after ec2-run-instances CLI (ec2run -h)
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--region", required=True, help="set ec2 region")
parser.add_argument("-z", "--availability_zone", required=True,  
                    help="set ec2 availability_zone")
parser.add_argument("-a", "--ami", required=True, help="set ec2 ami name")
parser.add_argument("-d", "--user_data", help="set user data input")
parser.add_argument("-f", "--user_data_file", help="set user data file")
parser.add_argument("-g", "--group", nargs='+', help="set ec2 security group")
parser.add_argument("-k", "--key", required=True, help="set ec2 keypair name")
parser.add_argument("-t", "--instance_type", required=True, help="set ec2 instance type")
parser.add_argument("-n", "--instance_count",
                    help="set ec2 maximum instances to launch")
parser.add_argument("-v", "--verbose", help="display verbose output",
                    action="store_true")
args = parser.parse_args()

if args.region:
    print "Region: %s" % args.region
if args.availability_zone:
    print "Availability Zone: %s" % args.availability_zone
if args.ami:
    print "AMI Name: %s" % args.ami
if args.region:
    print "User Data: %s" % args.user_data
if args.region:
    print "User Data File: %s" % args.user_data_file
if args.group:
    print "Security Group: %s" % args.group
if args.key:
    print "Keypair Name: %s" % args.key
if args.instance_type:
    print "Instance Type: %s" % args.instance_type
if args.instance_count:
    print "Max number of instances to launch: %s" % args.instance_count
if args.verbose:
    print "display verbose output"
