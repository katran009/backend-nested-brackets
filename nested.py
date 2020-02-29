#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "katran009, Demo by Piero"

import sys

# openers = {"(", "[", "{", "<", "*"}
# closers = {")", "]", "}", ">", "*"}

tokens_dict = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
    "*)": "(*",
}


def is_nested(line):
    """Validate a single input line for correct nesting"""
    stack = []
    token_counter = 0
    while line:
        # figure out what my token is this time thru the loop
        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        elif line.startswith("*)"):
            token = "*)"

        token_counter += 1
        line - line[len(token):]

        if token in tokens_dict.values():
            stack.append(token)
        elif token in tokens_dict.keys():
            # closer_index = closrs.index(token)
            expected_opener = tokens_dict[token]
            if stack.pop() != expected_opener:
                return "NO " + str(token_counter)
# while loop has new exited
# check if there is anything left on the stack
    if stack:
        # we haev junk left over, this is bad
        return "NO " + str(token_counter)

    # If we make it here, all is GOOD
    return "YES "


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    print("Testing for Nesting: {}".format(args[0]))
    with open(args[0]) as ifile:
        with open('output.txt', 'w') as ofile:
            for line in ifile:
                result_str = is_nested(line)
                # result_str = "NO {}".format(index) if index else "YES"
                print(result_str)
                ofile.write(result_str + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
