#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def square(n):
	'''function tha returns the square of passed integer'''
	return n**2

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2: # first parameter is the name of program
    	print 'At least one argument with integer number is needed'
    	exit(1)
    print square(int(sys.argv[1]))
