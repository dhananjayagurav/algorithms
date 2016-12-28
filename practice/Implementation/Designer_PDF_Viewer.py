problem from HakerRank
'''
Input Format

The first line contains space-separated integers describing the respective heights of each consecutive lowercase English letter (i.e., ).
The second line contains a single word, consisting of lowercase English alphabetic letters.

Constraints

    , where is an English lowercase letter.
    Word contains no more than letters.

Output Format

Print a single integer denoting the area of highlighted rectangle when the given word is selected. The unit of measurement for this is square millimeters (), but you must only print the integer.

Sample Input

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output

9

Explanation

We are highlighting the word abc:

    The tallest letter in abc is b, and . The selection area for this word is .

Note: Recall that the width of each character is .

'''

#!/bin/python

import sys


h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

let_height_map = {letters[i]:h[i] for i in range(26)}

ht = list()
w_l = list()

for w in word:
    ht.append(let_height_map[w])
    w_l.append(w)

print len(w_l) * max(ht) * 1 
