import sys
import re
from itertools import permutations

def digits_larger_than_number(number):
    """Function creates a string of digits larger a given digit.

    Args: number (int or string): single digit number

    Returns: a string of all the digits larger than the input
    """


    digit_string = '0'
    number = int(number)

    while number < 9:
        number += 1
        digit_string = digit_string + str(number)
    return digit_string


def pop_out_string(pop_out_this, original_string):
    """Function will remove all characters in one string from another string

    Args:
        pop_out_this (int or string): These are the characters to be remove.
        If int enter, it will be converted to a string
        original_string (string): String that needs stuff removed from it.


    Returns:
        String: All the chracters in the original that were not in the pop_out_this
    """
    regex_string = "[" + str(pop_out_this) + "]"

    return str(re.sub(regex_string, '', original_string))

def main(args):
    line = sys.stdin.readline()

    while line:
        pairing = str(line)
        pairing = pairing.replace(' ','')


        # Strip the ':' and the '!' to get the digits only as a string
        pairing_digits = ''.join(sorted(re.sub('[:!]', '', pairing)))

        # Get key of pairing as a string. It is before the :
        pairing_key = pairing.split(':')[0]

        # Get all information left of the '!'
        pairing_left = re.sub('[:]', '', (pairing.split('!')[0]))

        # Get all the digits other than the pairing key
        pairing_minus_key = pairing_digits.replace(pairing_key, '')
        pairing_minus_key = pairing_minus_key.strip()

        for i in range(1, (len(pairing_minus_key) + 1)):

            perms_list = [(pairing_key + ''.join(p)) for p in permutations(pairing_minus_key, i)]
            print (i)

            print (pairing_minus_key)
            print(perms_list)

        line = sys.stdin.readline()

if __name__ == '__main__':
    main(sys.argv)