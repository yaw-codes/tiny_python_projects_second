#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-10-26
Purpose: Crow's Nest -- choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')
    
    parser.add_argument('-s',
                        '--side',
                        help='set to starboard',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side
    

    article = ""
    
    if word[0] in "aeiouAEIOU":
        article = "an" if word[0].islower() else "An"
    else:
        article = "a" if word[0].islower() else "A"
        
    side_word = "starboard" if side else "larboard"

    print(f"Ahoy, Captain, {article} {word} off the {side_word} bow!")

# --------------------------------------------------
if __name__ == '__main__':
    main()
