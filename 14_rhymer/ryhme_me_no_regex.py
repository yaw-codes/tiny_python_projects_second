#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-12-23
Purpose: Making rhyming words
"""

import argparse
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='making rhyming words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()
    
    start, rest = stemmer(args.word)
    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print(f'Cannot rhyme "{args.word}"')
    
# --------------------------------------------------
def stemmer(word):
     """Return leading consonants (if any), and 'stem' of word"""
     word = word.lower()
     vowel = 'aeiou'
     
     vowel_pos = list(map(word.index,filter(lambda v: v in word,vowel)))
     
     if vowel_pos:
         first_v = min(vowel_pos)
         return(word[:first_v],word[first_v:])
     else:
         return(word, '')

# --------------------------------------------------    
def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')

# --------------------------------------------------
if __name__ == '__main__':
    main()
