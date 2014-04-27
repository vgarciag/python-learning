#!/usr/bin/env python
# -*- coding: UTF-8 -*-

print 'Printing a list with a while loop:'
j = ['one', 'two', 'three',]
while j:
	print j[0],
	j = j[1:]

print 'if ... elif ... else ... conditional branches:'
input_value = raw_input("Please enter an integer: ")
# print type(input_value)
# if type(input_value) is not int:
# 	print str(input_value) + ' is not an integer value. Exiting... '
# 	exit()

x = int(input_value)

if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
	print 'More'

print "for statements:"
print 'Measure some strings:'
words = ['cat', 'window', 'defenestrate']
print words
for w in words:
    print w, len(w)

print 'inserting a new element into looping list. It\'s needed to use a copy of a list list[:]...'
for w in words[:]:  # Loop over a slice copy of the entire list.
	if len(w) > 6:
		words.insert(0, w)

print words

print 'range() function: '
print 'range(10)             = ' + str(range(10))
print 'range(5, 10)          = ' + str(range(5, 10))
print 'range(0, 10, 3)       = ' + str(range(0, 10, 3))
print 'range(-10, -100, -30) = ' + str(range(-10, -100, -30))

print 'break and continue Statements, and else Clauses on Loops'
for i in words:
	print i
else:
	print "finally " + str(i)




