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
