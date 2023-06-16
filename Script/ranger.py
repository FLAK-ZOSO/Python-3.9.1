import sys

if __name__ == "__main__":
    print(', '.join(map(str, range(int(sys.argv[1]), int(sys.argv[2]) + 1, int(sys.argv[3])))))