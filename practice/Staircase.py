'''
For a structure like below 
     #
    ##
   ###
  ####
 #####
######
'''

#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(n):
    mystr = '#'+'#'*i
    print mystr.rjust(n)
