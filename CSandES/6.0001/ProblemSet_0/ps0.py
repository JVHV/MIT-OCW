#!/usr/bin/env python

import numpy

def xToTheY(base, expo):
    return base**expo

x = int (input("Enter number x: "))
y = int (input("Enter number y: "))
print "X**y = ", xToTheY(x, y)
print "log(x) = ", int(numpy.log2(x))

