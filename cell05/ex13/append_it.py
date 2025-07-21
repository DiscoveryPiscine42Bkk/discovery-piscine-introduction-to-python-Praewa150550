#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if len(args) == 0:
    print("none")
else:
    printed = False
    for word in args:
        if not word.endswith("ism"):
            print(word + "ism")
            printed = True
    if not printed:
        print("none")