import argparse
import sys

try:
     parser = argparse.ArgumentParser()
     parser.add_argument("user", help="",
                type=int)
    args = parser.parse_args()

    #user input from cmd line.
    print args.user**2

    #print all the sys argument passed from cmd line including the program name.
    print sys.argv

    #print the second argument passed from cmd line; Note it starts from ZERO
    print sys.argv[1]
except:
    e = sys.exc_info()[0]
    print e