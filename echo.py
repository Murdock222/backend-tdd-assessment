#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Cory, demo"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', help='text to manipulated')
    parser.add_argument('-u', action='store_true', help='convert text to uppercase')
    parser.add_argument('-l', action='store_true', help='convert text to lowercase')
    parser.add_argument('-t', action='store_true', help='convert text to titlecase')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    
    msg = ns.text
    
    if ns.t:
        msg = msg.title()
        
    if ns.l:
        msg = msg.lower()
    
    if ns.u:
        msg = msg.upper()
    
    
    
    print(msg)
    


if __name__ == '__main__':
    main(sys.argv[1:])
