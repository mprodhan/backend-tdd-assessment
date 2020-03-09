#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "mprodhan/madarp"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text."
        )
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument("-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true", help="covert text to lowercase")
    parser.add_argument("-t", "--title", action="store_true", help="convert text to titlecase")
    return parser

def main(args):
    """Implementation of echo"""
    parser = create_parser()
    name_space = parser.parse_args(args)
    result = name_space.text
    if name_space.upper:
        result = result.upper()
    if name_space.lower:
        result = result.lower()
    if name_space.title:
        result = result.title()
    return result

if __name__ == '__main__':
    main(sys.argv[1:])
