#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import site
import os


filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    print "File exected at python shell interactive mode: " + filename

print "User site packages:   " + site.getusersitepackages()
print "System site packages: " + str(site.getsitepackages())


site.getsitepackages()