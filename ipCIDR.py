#!/usr/bin/python

import sys
import argparse
from netaddr import *


def main(args):
	parser = argparse.ArgumentParser(description='Check if ip(s) in range(s) --- don\'t use -i and -I or -r and -R')
	igroup = parser.add_mutually_exclusive_group(required = True)
	igroup.add_argument('-i', '--ip',  help='ip to test')
	igroup.add_argument('-I', '--ipFile',  help='txt of ips, 1 per line')
	rgroup = parser.add_mutually_exclusive_group(required = True)
	rgroup.add_argument('-r', '--range',  help='range to check')
	rgroup.add_argument('-R', '--rangeFile',  help='file of ranges, csv with 2nd column name of range')
	parser.add_argument('-o', '--outputfile', help='name of file to output, otherwise stdout')
	
	args = parser.parse_args()
	
	rangeName = {}
	
	if args.ip:
		fips = [args.ip]
		try:
			IPAddress(args.ip)
		except:
			print("Not a valid ip address")
			sys.exit(1)
			
	if args.ipFile:
		try:
			fips = open(args.ipFile, 'r')
		except:
			print(args.ipFile + " does not exist. Please use full path if error persists")
			sys.exit(1)
		
	if args.range:
		try:
			range = IPNetwork(args.range)
			rangeIPs[range] = list(range)
			rangeName[range] = "N/A"
		except:
			print("Not a valid network range")
			sys.exit(1)
	
	count = 0
	if args.rangeFile:
		try:
			frange = open(args.rangeFile, 'r')
		except:
			print(args.rangeFile + " does not exist. Please use full path if error persists")
			sys.exit(1)
		print("Processing IP Ranges\n")
		for line in frange:
			line = line.split(",")
			try:
				range = IPNetwork(line[0])
				if len(line) > 1:
					name = line[1]
				else:
					name = "N/A"
				rangeName[range] = name.strip()
			except:
				print(line[0] + " is not a valid CIDR range.  Will not be included in search")
				ans = "Y"
				while ans != "y" and ans != "n":
					ans = input("Would you like to continue anyway? (Y/N) ")
					ans = ans.lower()
				if ans == "n":
					sys.exit(1)
			count = count + 1
			if count % 25 == 0:
				print("Processed " + str(count) + " ranges\n")
			
			
	pflag = True
	if args.outputfile:
		fout = open(args.outputfile, 'w+')
		pflag = False

	count = 0
	flag = False
	print ("Checking IPs\n")
	for ip in fips:
		flag = False
		try:
			ip = IPAddress(ip)
			for range in rangeName:
				if ip >= range[0] and ip <= range[-1]:
					s = str(ip) + "," + str(range) + "," + rangeName[range]
					if pflag:
						print(s)
					else:
						fout.write(s + "\n")
					flag = True
					break
			if flag == False:
				s = str(ip) + " not in ranges"
				if pflag:
					print(s)
				else:
					fout.write(s + "\n")
		except:
			print(ip.strip() + " is not a valid IP address.  Will not be included in search")
		count = count + 1
		if count % 100 == 0:
			print("Processed " + str(count) + " IPs\n")
	
	
if __name__ == "__main__":
	if sys.version_info < (3,0):
		print("Must use python 3.0 or +")
		sys.exit(1)
	print("netaddr module must be installed for this script to run correctly!\n")
	main(sys.argv)
	