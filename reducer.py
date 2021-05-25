#!/usr/bin/env python

import sys

sum_of_out_degree = 0
number_of_timestamps = 0
previous_i = None
previous_time = None

print('%s\t%s' % ('Node', 'OutDegree'))

for line in sys.stdin:
    try:
        i, timestamp = line.strip().split('\t')

        if previous_i == None:
            previous_i = i
            previous_time = timestamp
            sum_of_out_degree += 1
            number_of_timestamps += 1
        elif previous_i == i:
            sum_of_out_degree += 1
            if previous_time != timestamp:
                number_of_timestamps += 1
                previous_time = timestamp
        else:
            print('%s\t%s' % (previous_i, sum_of_out_degree//number_of_timestamps))
            previous_i = i
            previous_time = timestamp
            sum_of_out_degree = 1
            number_of_timestamps = 1
    except ValueError:
        continue

print('%s\t%s' % (previous_i, sum_of_out_degree//number_of_timestamps))
