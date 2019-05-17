#!/usr/bin/python
"""TODO(prasana): DO NOT SUBMIT without one-line documentation for main.
A simple main function
TODO(prasana): DO NOT SUBMIT without a detailed description of main.
"""

import sys # sys.argv
'''
import flags
FLAGS = flags.FLAGS
'''

def print_str(s):
	print (s+"\n")

def fact(n):
	if n <= 1:
		return(n)
	else:
		return(n*fact(n-1))

def reverse_file(f):
	return

def revese_str(s):
	return v

def help():
	help = sys.argv[0] 
	help += " [--help]" 
	help += " [--factorial=nn]"
	print_str(help)

def main(argv):
	if len(argv) <= 1 or argv[1] == "--help":
	  help()
	return

## main loop
main(sys.argv)
