#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest


class Test002(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "-----test02 start-----"
        print ""

    @classmethod
    def tearDownClass(cls):
        print "-----test02 end-----"

    def test_001(self):
        print "test001"

    def test_002(self):
        print "test002"

    def test_003(self):
        print "test003"


if __name__ == '__main__':
    unittest.main(verbosity=2)
