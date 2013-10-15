#!/usr/bin/env python
"""Class-less Python program with main function.
"""
import sys


def parse_args(argv=None):
    """Return length of argv array, returns 0 if argv is None
    """
    if argv is None:
        argv = []
    return len(argv)

if __name__ == '__main__':
    print parse_args(sys.argv)
