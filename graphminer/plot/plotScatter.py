import matplotlib.pyplot as plt
import sys

# degree_file = file('../data/1_degreedist.csv', 'r')
# degree_file = file('../data/3_component_size_dist.csv', 'r')


def main(argv):
    degree_file = file(argv[0], 'r')
    degrees = []
    degree_cnt = []

    line = degree_file.readline()
    while line:
        line = line.strip()
        line = line.split(',')
        degrees.append(float(line[0]))
        degree_cnt.append(abs(float(line[1])))
        line = degree_file.readline()

    plt.figure()
    ax = plt.gca()
    ax.scatter(degrees, degree_cnt)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.grid(True)
    plt.savefig('../img/' + argv[1])
    print "END"

if __name__ == '__main__':
    main(sys.argv[1:])
