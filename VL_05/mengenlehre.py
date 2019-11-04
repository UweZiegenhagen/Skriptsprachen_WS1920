# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:25:20 2019

@author: Uwe Ziegenhagen
"""

a = {3, 5, 7, 12, 14, 17, 19, 23}
b = {3, 5, 17}
c = {12, 14, 17, 24}
d = {5, 7, 19}
e = {7, 12, 19}
f = {5, 19, 7}

print(b.issubset(a))

print(c.issubset(a))

print(e.issubset(a))

print(b.issubset(c))

print(e.issubset(c))

print(f == d)

print(f - d)

print(f - d == set())