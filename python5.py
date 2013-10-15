#!/usr/bin/env python
"""Python program with Class and main function.
"""
import sys


class Main(object):
    """Main class to encapsulate logic
    """
    def __init__(self, argv=None):
        """Initializer

        Keyword Arguments:
        argv - list of arguments
        """
        self._argv = argv

    def parse_args(self):
        """Return length of argv array, returns 0 if argv is None
        """
        if self._argv is None:
            return 0
        else:
            return len(self._argv)

if __name__ == '__main__':
    print Main(sys.argv).parse_args()
