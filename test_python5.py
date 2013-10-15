#!/usr/bin/env python
import unittest

import python5


class Python5TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_argsNone(self):
        argv = None
        myobj = python5.Main(argv)
        self.assertEqual(myobj.parse_args(), 0)

    def test_parse_argsEmpty(self):
        argv = []
        myobj = python5.Main(argv)
        self.assertEqual(myobj.parse_args(), 0)

    def test_parse_argsOptions(self):
        argv = ['myname.py', '-a', 'arg_a', '-b', 'arg_b', 'one', 'two']
        myobj = python5.Main(argv)
        expect = len(argv)
        self.assertEqual(myobj.parse_args(), expect)

if __name__ == '__main__':
    unittest.main()
