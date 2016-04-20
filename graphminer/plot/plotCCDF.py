#!/usr/bin/env python

# @Author: Silun Wang
# @Andrew id: silunw
# @Date: 4/16/16 15:01

import matplotlib.pyplot as plt
import sys

def main(argv):
    degree_file = file(argv[0], 'r')
    degrees = []
    CCDF = []
    cnt = 1
    line = degree_file.readline()
    while line:
        line = line.strip()
        line = line.split(',')
        degrees.append(float(line[1]))
        CCDF.append(cnt)
        cnt += 1
        line = degree_file.readline()

    degrees.sort()
    CCDF.reverse()
    for x in CCDF:
        x /= (len(CCDF) + 0.0)

    plt.figure()
    ax = plt.gca()
    plt.plot(degrees, CCDF)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.grid(True)
    plt.savefig('../img/' + argv[1])
    print "END"

if __name__ == '__main__':
    main(sys.argv[1:])
