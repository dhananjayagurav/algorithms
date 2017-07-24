#Below program counts frequency of words in a file. 

import re
import operator
import collections

mydict = dict()

with open ('myTextFile.txt','r') as infile:
    for line in infile:
        line = re.sub('[!@#$]', '', line)
        lst = list()
        lst = line.lower().split()
        for word in lst:
            word = ''.join(x for x in word if ord(x) < 128)
            if not word in mydict:
                mydict[word] = 1
            else:
                mydict[word] += 1

#Implementation using operator library
sorted_mydict = sorted(mydict.items(), key=operator.itemgetter(1))
print ("operator library implementation")
for val in reversed(sorted_mydict[-10:]):
    print val[0],val[1]

#Implemetation using collections library
cnt =  collections.Counter(mydict)       
print ("collection library implementation")
for k,v in cnt.most_common(10):
    print k,v
