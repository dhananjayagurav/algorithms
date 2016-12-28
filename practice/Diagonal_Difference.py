#!/bin/python

import sys

n = int(raw_input().strip())
a = list()

for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
sum1 = 0
sum2 = 0
i = 0

    
for lst in a:
    sum1 += lst[i]
    sum2 += lst[n-1-i]
    i += 1

print abs(sum1-sum2)
