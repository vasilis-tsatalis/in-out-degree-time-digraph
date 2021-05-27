#!/usr/bin/env python

import sys

sum_of_degree = 0
number_of_timestamps = 0
previous_node = None
previous_degree_type = None
previous_time = None

print('%s\t%s\t%s' % ('Node', 'Degree Type', 'Value'))

for line in sys.stdin:
    try:
        degree_type, node, timestamp = line.strip().split('\t')

        if previous_degree_type == None:
            previous_node = node
            previous_time = timestamp
            previous_degree_type = degree_type
            sum_of_degree += 1
            number_of_timestamps += 1
        elif previous_node == node and previous_degree_type == degree_type:
            sum_of_degree += 1
            if previous_time != timestamp:
                number_of_timestamps += 1
                previous_time = timestamp
        else:
            print('%s\t%s\t%s' % (previous_node, previous_degree_type, sum_of_degree//number_of_timestamps))
            previous_node = node
            previous_time = timestamp
            previous_degree_type == degree_type
            sum_of_degree = 1
            number_of_timestamps = 1
    except ValueError:
        continue

print('%s\t%s\t%s' % (previous_node, previous_degree_type, sum_of_degree//number_of_timestamps))
