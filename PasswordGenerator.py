#!/usr/bin/python3

import argparse
import string
import random

parser = argparse.ArgumentParser(
    prog='CLI Password Generator',
    description='Generates the password based on the given arguments',
)

parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password')
parser.add_argument('-d', '--digits', action='store_true', help='Include digits or not')
parser.add_argument('-s', '--special', action='store_true', help='Include special characters or not')

args = parser.parse_args()

def genpass(n=args.length, include_digits=args.digits, include_special=args.special):
    if n >= 8:
        letters = string.ascii_letters 
        digits = string.digits if include_digits else ''
        special_characters = string.punctuation if include_special else ''

        all_characters = letters + digits + special_characters

        password = ''.join(random.choice(all_characters) for _ in range(n))
        print("\nGenerated password:", password)
        
    else:
        print("\nPassword length should be at least 8 characters")

genpass()