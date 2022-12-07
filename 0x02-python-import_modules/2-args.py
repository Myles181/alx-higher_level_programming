#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 1
    length = len(sys.argv)
    if length > 1:
        print("{} arguments:".format(length - 1))
        for item in sys.argv[1:]:
            print("{}: {}".format(count, item))
            count += 1
    else:
        print("{} arguments.".format(length - 1))
