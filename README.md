# Python-check-IPs-in-Ranges
Take an ip or list of IPs and see if it is in a range or list of ranges


Arguments:
-i a single ip to check
-I a list of ips 1 per line to check
-r an ip range to check against
-R a list of IP ranges to check against
-o the outputfile - if not entered, will print to stdout

the file given in -R can be a csv where column 1 is the CIDR range and column 2 is the the name of the range.  This can be used to match an ip to the name of the range

example input file:
192.168.0.0/24,dev
192.168.1.0/24,dmz

output:
192.168.0.5,192.168.0.0/24,dev
