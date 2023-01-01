#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-12-29
Purpose: Rock the Casbah
"""

import argparse
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type = argparse.FileType('rt'),
                        help='Input file')


    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*')
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()
    blanks = re.findall('(<([^<>]+)>)',text)
    
    
    if not blanks:
        sys.exit(f'"{args.file.name}" has no placeholders.')
        
    templ = 'Give me {} {}: '
    
    for placeholder,pos in blanks:
        article = "an" if pos.lower()[0] in 'aeiou' else 'a'
        answer =  inputs.pop(0) if inputs else input(templ.format(article,pos))
        text =re.sub(placeholder,answer,text,count=1)
        
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
