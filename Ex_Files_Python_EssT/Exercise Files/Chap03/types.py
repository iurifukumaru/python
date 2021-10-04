#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

xxx = (1, 'dois', [3, 'Three'], 4.0, 5)
print('x is {}'.format(xxx))
print(type(xxx))
print(type(xxx[3]))
print(id(xxx[0]))

x = '''seven {1}" "{0}'''.format(8, 9).upper()
print('x is {}'.format(x))
print(type(x))

y = Decimal('.1')
z = Decimal('.3')
xx = y * 3 - z
print(xx)
print(type(xx))