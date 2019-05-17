#!/usr/bin/python
"""TODO(prasana): DO NOT SUBMIT without one-line documentation for main.
A simple main function
TODO(prasana): DO NOT SUBMIT without a detailed description of main.
"""

import sys # sys.argv
import argparse ## for argument parsing
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

## deprecated
def help():
	help = sys.argv[0] 
	help += " [--help]" 
	help += " [--factorial=nn]"
	print_str(help)

def flagHandler():
	parser = argparse.ArgumentParser()
	help_str = "calculate factorial"
	parser.add_argument("factorial", type=int, help=help_str)
	args = parser.parse_args()
	return args

def main(argv):
	cli_args=flagHandler()
	if cli_args.factorial:
		f=fact(cli_args.factorial)
		print_str(str(f))
	return

## main loop
main(sys.argv)
