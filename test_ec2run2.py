#!/usr/bin/env python
import unittest

import ec2run2.py


class Python4TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_argsNone(self):
        argv = None
        self.assertEqual(python4.parse_args(argv), 0)

    def test_parse_argsEmpty(self):
        argv = []
        self.assertEqual(python4.parse_args(argv), 0)

    def test_parse_argsOptions(self):
        argv = ['myname.py', '-a', 'arg_a', '-b', 'arg_b', 'one', 'two']
        expect = len(argv)
        self.assertEqual(python4.parse_args(argv), expect)

if __name__ == '__main__':
    unittest.main()
