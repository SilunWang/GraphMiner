#!/usr/bin/env python

# @Author: Silun Wang
# @Andrew id: silunw
# @Date: 4/19/16 22:30

import matplotlib.pyplot as plt
import sys


def main(argv):
    degree_file = file(argv[0], 'r')
    degrees = []
    PDF = []
    line = degree_file.readline()
    cnt = 0
    while line:
        line = line.strip()
        line = line.split(',')
        degrees.append(float(line[0]))
        PDF.append(float(line[1]))
        cnt += int(line[1])
        line = degree_file.readline()

    degrees.sort()
    PDF.reverse()

    plt.figure()
    ax = plt.gca()
    plt.plot(degrees, PDF)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.grid(True)
    plt.savefig('../img/' + argv[1])
    print "END"

if __name__ == '__main__':
    main(sys.argv[1:])