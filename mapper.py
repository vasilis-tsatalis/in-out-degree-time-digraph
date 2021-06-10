#!/usr/bin/env python
# coding=utf-8

import argparse
import sys
import csv


def main(args, filename):

    reader = csv.reader(filename, delimiter=args.delimiter)

    next(reader)

    for line in reader:
        try:
            i, j, timestamp = line

            if args.degree == 'in':
                type = 'IN'
                node = j
            elif args.degree == 'out':
                type = 'OUT'
                node = i
            else:
                ValueError

            print('%s\t%s\t%s' % (node, timestamp, type))

        except ValueError:
            continue

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Dynamic Network Graph Input - Output Degree Calculation')
    parser.add_argument('--degree', type=str, dest='degree', choices = ['in', 'out'], help='Degree type', required=True)
    parser.add_argument('--separator', type=str, dest='delimiter', help='Delimiter character', default=',')
    args = parser.parse_args()

    main(args, sys.stdin)
