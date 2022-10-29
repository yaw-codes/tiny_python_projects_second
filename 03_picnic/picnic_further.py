#!/usr/bin/env python3
"""
Author : Stanley Yaw Appiah <appstan2003@gmail.com>
Date   : 2022-10-26
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs="+",
                        help='Item(s) to bring')
    
    parser.add_argument('-d',
                        '--delineator',
                        help='at a str that separates the values',
                        metavar='str',
                        type=str,
                        default=' ')


    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')
    parser.add_argument('-o',
                        '--oxford',
                        help='with to add the oxford comma',
                        action='store_true')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    sort_flag = args.sorted
    ox_flag = args.oxford
    deli = args.delineator
    
    

    if len(deli) == 1: 
        if sort_flag:
            items.sort()
            if len(items) == 1:
                print(f"You are bringing {deli.join(items)}.")
            elif len(items) == 2:
                print(f"You are bringing {deli.join(items)}.")
            elif len(items) > 2:
                if ox_flag:
                    print(
                        f"You are bringing {deli.join(items[:-1]) + deli + items.pop()}."
                    )
                else:
                    print(
                        f"You are bringing {deli.join(items[:-1]) + deli + items.pop()}."
                    )
        else:
            if len(items) == 1:
                print(f"You are bringing {deli.join(items)}.")
            elif len(items) == 2:
                print(f"You are bringing {deli.join(items)}.")
            elif len(items) > 2:
                if ox_flag:
                    print(
                        f"You are bringing {deli.join(items[:-1]) +deli+ items.pop()}."
                    )
                else:
                    print(
                        f"You are bringing {deli.join(items[:-1]) +deli+ items.pop()}."
                    )
    else:
        if sort_flag:
            items.sort()
            if len(items) == 1:
                print(f"You are bringing {''.join(items)}.")
            elif len(items) == 2:
                print(f"You are bringing {' and '.join(items)}.")
            elif len(items) > 2:
                if ox_flag:
                    print(
                        f"You are bringing {', '.join(items[:-1]) +' and '+ items.pop()}."
                    )
                else:
                    print(
                        f"You are bringing {', '.join(items[:-1]) +', and '+ items.pop()}."
                    )
        else:
            if len(items) == 1:
                print(f"You are bringing {''.join(items)}.")
            elif len(items) == 2:
                print(f"You are bringing {' and '.join(items)}.")
            elif len(items) > 2:
                if ox_flag:
                    print(
                        f"You are bringing {', '.join(items[:-1]) +' and '+ items.pop()}."
                    )
                else:
                    print(
                        f"You are bringing {', '.join(items[:-1]) +', and '+ items.pop()}."
                    )

# --------------------------------------------------
if __name__ == '__main__':
    main()
