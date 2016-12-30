#HackerRank problem
'''
Consider two sets of positive integers, and . We say that a positive integer, , is between sets and if the following conditions are satisfied:

    All elements in are factors of .
    is a factor of all elements in .

Given and , find and print the number of integers (i.e., possible 's) that are between the two sets.

Input Format

The first line contains two space-separated integers describing the respective values of (the number of elements in set ) and (the number of elements in set ).
The second line contains distinct space-separated integers describing .
The third line contains distinct space-separated integers describing .

Constraints

Output Format

Print the number of integers that are considered to be between and .

Sample Input

2 3
2 4
16 32 96

Sample Output

3

'''

#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

n_start = a[len(a)-1]
n_end = b[0]
f_a = list()
f_b = list()

for i in range (n_start,n_end+1):
    f1 = 0
    for j in a:
        if i%j != 0:
            f1 = 1
    if f1 == 0:    
        f_a.append(i)
    f2 = 0
    for k in b:
        if k%i != 0:
            f2 = 1
    if f2 == 0:    
        f_b.append(i)
        
if (n_start == n_end+1):
    print 0
else:
    print len(set(f_a).intersection(set(f_b)))
