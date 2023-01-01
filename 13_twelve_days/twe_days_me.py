#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-12-21
Purpose: Twelve days Of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)



    parser.add_argument('-n',
                        '--num',
                        help='number of Days',
                        metavar='number',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    print("\n\n".join(map(verse,range(1,args.num+1))),file=args.outfile)
    

# --------------------------------------------------
def verse(day):
    """ A verse for the day of christmas"""
    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]
    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
        
    ]
    lines = [
        f"On the {ordinal[day-1]} day of Christmas,",
        "My true love gave to me,"
        
    ]
    lines.extend(reversed(gifts[:day]))
    
    if day > 1:
        lines[-1] = "And " + lines[-1].lower()
    
    return "\n".join(lines)
# --------------------------------------------------
def test_verse():
    """Test verse"""
    assert verse(1) == "\n".join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == "\n".join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle doves,', 'And a partridge in a pear tree.'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
