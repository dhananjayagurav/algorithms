#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
acs = 0
bcs = 0

if (a0 > b0):
    acs += 1
if (a1 > b1):
    acs += 1
if (a2 > b2):
    acs += 1

if (a0 < b0):
    bcs += 1
if (a1 < b1):
    bcs += 1
if (a2 < b2):
    bcs += 1

print acs,bcs
