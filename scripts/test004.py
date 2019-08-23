#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest


class Test004(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "-----test04 start-----"
        print ""

    @classmethod
    def tearDownClass(cls):
        print "-----test04 end-----"

    def test_001(self, expect=None):
        print "test001"
        self.assertEqual(None, expect)

    def test_002(self,expect="test002"):
        print "test002"
        self.assertIn("test",expect)

    def test_003(self):
        print "test003"


if __name__ == '__main__':
    unittest.main(verbosity=2)
