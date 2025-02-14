#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-11-01
Purpose: Howler
"""

import argparse
import os
import io
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='return uppercase text given to it',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='input string or file')
    
    parser.add_argument('-l',
                        '--lower',
                        help='to use lowercase instad of upper',
                        action='store_true')
    

    parser.add_argument('-o',
                        '--outfile',
                        help='output filename',
                        metavar='str',
                        type=str,
                        default='')
    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text) as file:
            args.text = file.read().rstrip()
    else:
        args.text = io.StringIO(args.text + "\n")
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    

    out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    for line in args.text:
        if args.lower:
            out_fh.write(line.lower())
        else:   
            out_fh.write(line.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
