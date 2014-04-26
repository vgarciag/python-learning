#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a = ['spam', 'eggs', 100, 1234]
print 'Original: ' + str(a)


print 'Accesing througt index: '
print a[0]
print a[3]
print a[-2]
print a[1:-1]
print a[:2] + ['bacon', 2*2]
print 3*a[:3] + ['Boo!']

print 'Modifications in lists: '
# Replace some items:
a[0:2] = [1, 12]
print a

# Remove some:
a[0:2] = []
print a

# Insert some:
a[1:1] = ['bletch', 'xyzzy']
print a

# Insert (a copy of) itself at the beginning
a[:0] = a
print a

# Clear the list: replace all items with an empty list
a[:] = []
print a


print 'Nested lists: '

q = [2, 3]
p = [1, q, 4]
print len(p)

print p[1]

print p[1][0]

p[1].append('xtra')     # See section 5.1
print p

print q

