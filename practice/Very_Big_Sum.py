#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

#For  big aaray sums using directly python sum function has considerable performnace gaim over using for loop
print sum(arr)
