import sys, getopt

def main(argv):
    input_file = file(argv[0])
    line = input_file.readline()
    while line:
        line = line.strip()
        arr = line.split()
        print arr[0] + ',' + arr[1]
        line = input_file.readline()

if __name__ == '__main__':
    main(sys.argv[1:])
