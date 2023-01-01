#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-12-13
Purpose: Bottles
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    for n in range(args.num,0,-1):
        print(verse(n),end="\n" *(2 if n>1 else 1))


# --------------------------------------------------
def verse(bottle):
    '''Sing a verse'''
    next_bottle = bottle - 1
    s_1 = "" if bottle == 1 else "s"
    s_2 = "" if next_bottle == 1 else "s"

    last_bottle = "No more" if next_bottle == 0 else next_bottle
    return '\n'.join([
        f"{bottle} bottle{s_1} of beer on the wall,",
        f"{bottle} bottle{s_1} of beer,", f"Take one down, pass it around,",
        f"{last_bottle} bottle{s_2} of beer on the wall!"
    ])


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == "\n".join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == "\n".join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
