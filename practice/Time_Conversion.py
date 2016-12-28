# problem source Hackerrank

'''
Given a time in -hour AM/PM format, convert it to military (-hour) time.

Note: Midnight is on a -hour clock, and on a -hour clock. Noon is on a -hour clock, and on a -hour clock.

Input Format

A single string containing a time in -hour clock format (i.e.: or ), where and .

Output Format

Convert and print the given time in -hour format, where .

Sample Input

07:05:45PM

Sample Output

19:05:45

'''


#!/bin/python

import sys


time = raw_input().strip()

def convert_hour(hr,ampm):
    if ampm == 'AM':
        if hr == '12':
            return '00'
        else:
            return hr
    elif ampm == 'PM':
        if hr == '12':
            return '12'
        else:
            hr = int(hr) + 12
            return hr

hr,mins,sec = time.split(":")
ampm = sec[2:]
final_sec = sec[:2]
final_hour = convert_hour(hr,ampm)
if final_hour < 10:
    final_hour = '0' + str(final_hour)
final_min = mins

print str(final_hour) + ':' + str(final_min) + ':' + str(final_sec)
