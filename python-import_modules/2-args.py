#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_count = len(sys.argv) - 1

    if args_count == 0:
          print(f"{args_count} argument.")
    elif args_count == 1:
        print(f"{args_count} argument:")
        print(f"{args_count}:", sys.argv[1])
    else:
        print(f"{args_count} arguments:")
        arguments_names = sys.argv[1:]
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
