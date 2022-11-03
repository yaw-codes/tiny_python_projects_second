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
                        nargs="+",
                        type=str,
                        help='input string or file')
    
    parser.add_argument('-l',
                        '--lower',
                        help='to use lowercase instad of upper',
                        action='store_true')
    

    parser.add_argument('-o',
                        '--outdir',
                        help='output filename',
                        metavar='str',
                        type=str,
                        default='')
    args = parser.parse_args()
    
    arg_files = []
    for wordline in args.text:
        if os.path.isfile(wordline):
            with open(wordline) as file:
                arg_files.append(file.read().rstrip())
        else:
            arg_files.append(wordline + "\n")
    
    args.text = arg_files
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    

    out_fh = open(args.outdir, "wt") if args.outdir else sys.stdout
    for line in args.text:
        if args.lower:
            out_fh.write(line.lower() + "\n")
        else:   
            out_fh.write(line.upper() + "\n")
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
