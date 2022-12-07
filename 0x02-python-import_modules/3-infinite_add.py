#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    sum = 0

    if len(argv) > 1:
        for item in argv:
            if item != argv[0]:
                sum += int(argv[i])
            i += 1
    print(sum)
