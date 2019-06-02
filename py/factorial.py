#!/usr/bin/python
"""TODO(prasana): DO NOT SUBMIT without one-line documentation for main.
A simple main function
TODO(prasana): DO NOT SUBMIT without a detailed description of main.
"""

import sys # sys.argv
import argparse ## for argument parsing

def print_str(s):
	print (str(s))

def fact(n, verbose):
	if n <= 1:
		return n
	else:
		if verbose:
			print_str(str(n)+"*"+str(n-1))
		return (n*fact(n-1, verbose))

def reverse_file(f):
	return

def revese_str(s):
	return v

def flagHandler():
	parser = argparse.ArgumentParser()
	help_str = "calculate factorial"
	parser.add_argument("factorial", type=int, help=help_str)
	parser.add_argument('--verbose', '-v',  action='count')
	args = parser.parse_args()
	return args

def main(argv):
	cli_args=flagHandler()
	if cli_args.factorial:
		f = fact(cli_args.factorial, cli_args.verbose)
		print_str(f)
	return

## main loop
main(sys.argv)
