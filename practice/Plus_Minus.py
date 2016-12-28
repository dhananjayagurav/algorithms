#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
p_cnt = 0
n_cnt = 0
z_cnt = 0

for i in arr:
    if i < 0:
        n_cnt += 1
    elif i == 0:
        z_cnt += 1
    elif i > 0:
        p_cnt += 1

print float(p_cnt)/n
print float(n_cnt)/n
print float(z_cnt)/n
