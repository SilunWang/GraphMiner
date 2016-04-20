#!/usr/bin/env python

# @Author: Silun Wang
# @Andrew id: silunw
# @Date: 4/16/16 15:34

import matplotlib.pyplot as plt
import sys


def main(argv):
    degree_file = file(argv[0], 'r')
    triangle_file = file(argv[1], 'r')

    degrees = {}
    triangles = {}

    line = degree_file.readline()
    while line:
        line = line.strip()
        line = line.split(',')
        degrees[line[0]] = float(line[1])
        line = degree_file.readline()

    line = triangle_file.readline()
    while line:
        line = line.strip()
        line = line.split(',')
        triangles[line[0]] = float(line[1])
        line = triangle_file.readline()

    degree_arr = []
    triangle_arr = []

    for key in degrees:
        degree_arr.append(degrees[key])
        triangle_arr.append(triangles[key])

    plt.figure()
    ax = plt.gca()
    ax.scatter(triangle_arr, degree_arr, s=10)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.grid(True)
    plt.xlim([min(triangle_arr), max(triangle_arr)])
    plt.ylim([min(degree_arr), max(degree_arr)])
    plt.savefig('../img/' + argv[2])
    # print min(triangle_arr), max(triangle_arr)
    # print min(degree_arr), max(degree_arr)
    # print triangle_arr
    # plt.show()
    print "END"

if __name__ == '__main__':
    main(sys.argv[1:])
