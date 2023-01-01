#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-12-03
Purpose: telephone
"""

import argparse
import os 
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='telephony',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    
    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args =  parser.parse_args()
    
    if not (0 <= args.mutations <= 1):
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1' )
        
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    random.seed(args.seed)
    len_text = len(text)
    
    alpha = ''.join(sorted(string.ascii_letters+string.punctuation))
    num_mut = round(len_text * args.mutations)
    
    new_text = text
    
    for i in random.sample(range(len_text),num_mut):
        new_char = random.choice(alpha.replace(new_text[i], ""))
        new_text = new_text[:i]+new_char+new_text[i+1:]
        
    print(f'You said: "{text}"\nI heard : "{new_text}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
