"""TODO(prasana): DO NOT SUBMIT without one-line documentation for main.
A simple main function
TODO(prasana): DO NOT SUBMIT without a detailed description of main.
"""

import sys

'''
import flags
FLAGS = flags.FLAGS
'''

def help():
  help = sys.argv[0] + "[ --help]" + " [--factorial=nn]"
  print(help)


def main(argv):
  """if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
    """
  if len(argv) <= 1 or argv[1] == "--help":
    help()
  return

## main loop
main(sys.argv)
