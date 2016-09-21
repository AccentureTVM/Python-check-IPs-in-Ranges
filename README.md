# Python-check-IPs-in-Ranges
Take an ip or list of IPs and see if it is in a range or list of ranges

PREREQ: Most have netaddr module installed

https://pypi.python.org/pypi/netaddr

Arguments:<br />
-i a single ip to check<br />
-I a list of ips 1 per line to check<br />
-r an ip range to check against<br />
-R a list of IP ranges to check against<br />
-o the outputfile - if not entered, will print to stdout<br />

the file given in -R can be a csv where column 1 is the CIDR range and column 2 is the the name of the range.  This can be used to match an ip to the name of the range

example input file:<br />
192.168.0.0/24,dev<br />
192.168.1.0/24,dmz<br />

output:<br />
192.168.0.5,192.168.0.0/24,dev<br />
