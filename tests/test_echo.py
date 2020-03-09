#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import sys
import subprocess

# Your test case class goes here
class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()
        self.pystring = "python"
        if sys.version_info[0] == 2:
            self.pystring = "python2"

    def test_help(self):
        process = subprocess.Popen(
            [self.pystring, "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf8")
        with open("./USAGE", "r") as f:
            usage = f.read()
        self.assertEquals(stdout, usage)

    def test_all_of_the_above(self):
        args = ["-tul", "hELLo worLD"]
        name_space = self.parser.parse_args(args)
        self.assertTrue(name_space.upper)
        self.assertTrue(name_space.lower)
        self.assertTrue(name_space.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_short(self):
        args = ["-u", "hello world"] 
        name_space = self.parser.parse_args(args)
        self.assertTrue(name_space.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_short(self):
        args = ["-l", "Hello World"]
        name_space = self.parser.parse_args(args)
        self.assertTrue(name_space.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ["-t", "hello world"]
        name_space = self.parser.parse_args(args)
        self.assertTrue(name_space.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ["--upper", "hello world"]
        name_space = self.parser.parse_args(args)
        self.assertTrue(name_space.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_long(self):
        args = ["--lower", "Hello World"]
        name_space = self.parser.parse_args(args)
        self.assertTrue(name_space.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_long(self):
        args = ["--title", "hello world"]
        name_space = self.parser.parse_args(args)
        self.assertTrue(name_space.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
