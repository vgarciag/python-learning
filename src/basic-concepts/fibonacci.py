#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 1000:
	# a trailing comma avoid new line in print
	print b,
	a, b = b, a+b


