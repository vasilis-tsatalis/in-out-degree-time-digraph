#!/usr/bin/env python

import sys
import csv
 
reader = csv.reader(sys.stdin, delimiter=',')
 
next(reader)

for line in reader:
    try:
        i, j, timestamp = line

        print('%s\t%s' % (i, timestamp))
        #print('%s\t%s\t%s' % (j, timestamp, 'IN'))

    except ValueError:
        continue
