#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-11-10
Purpose: Apples and Bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitue',
                        metavar='vowel',
                        choices=["a", "e", "i", "o", "u"],
                        type=str,
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text) as file:
            args.text = file.read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    text = args.text
    vowel =args.vowel
    
    #create a new list to hold the chaaracters for the transformed text
   
    
    for v in "aeiou":
        text = text.replace(v, vowel).replace(v.upper(),vowel.upper() )
 
    print(text)
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
