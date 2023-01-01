#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-12-29
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs(for testing)',
                        metavar='input',
                        type=str,
                        nargs='*')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.file.read().rstrip()
    inputs = args.inputs
    had_placeholder = False

    templ = "Give me {} {}: "
    
    while True:
        brackets = find_brackets(text)
        if not brackets:
            break
        
        start, stop = brackets
        placeholder = text[start:stop+1]
        pos = placeholder[1:-1]
        article = 'an' if pos.lower()[0] in 'aeiou' else 'a'
        answer = inputs.pop(0) if inputs else input(templ.format(article,pos))
        text = text[0:start] + answer + text [stop + 1]
        had_placeholder = True
        
    if had_placeholder:
        print(text)
    else:
        sys.exit(f'"{args.file.name} has no placeholders. "')
    
    
    print(text)

# --------------------------------------------------
def test_find_brackets():
    """Test for findind angle brackets"""
    assert find_brackets('') is None
    assert find_brackets('<>') is None
    assert find_brackets('<x>') == (0, 2) 
    assert find_brackets('foo <bar> baz') == (4, 8)
   
# --------------------------------------------------
def find_brackets(text):
    """Find angle brackets"""
    start = text.index('<') if '<' in text else -1
    stop = text.index('>') if start >= 0 and '>' in text[start+2:] else -1
    return(start,stop) if start >= 0 and stop >= 0 else None
# --------------------------------------------------
if __name__ == '__main__':
    main()
