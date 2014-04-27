#!/usr/bin/env python
# -*- coding: UTF-8 -*-

long_string = '''This is a test
of a large string
'''

print long_string

print 'The lenght of \'long_string\' string variable is: ' + str(len(long_string))

print 'Print from 4th character to the end of string: ' + long_string[3:]

print 'String repeated with \'*\' operator: ' + 2*long_string
