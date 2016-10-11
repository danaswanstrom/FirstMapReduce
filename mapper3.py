import sys
import re

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


        # Strip the ':' and the '!' to get the digits only as a string
        pairing_digits = re.sub('[:!]', '', pairing)

        # Get key of pairing as a string. It is before the :
        pairing_key = pairing.split(':')[0]

        # Get all information left of the '!'
        pairing_left = re.sub('[:]', '', (pairing.split('!')[0]))

        # Find the maximum digit value in the pairing information
        max_digit_value = max([x for x in pairing_digits])

        digits_len = len(pairing_digits)

        # The max export key will never be larger than a repitition of the max digit
        max_export_key = int(str(max_digit_value) * digits_len)
        # Next line uses the extra digits and adds a 0 because 0 will also never be used
        export_key_illegal_digits = digits_larger_than_number(max_digit_value) + '0'
        export_key_illegal_digits_regex = "[" + str(export_key_illegal_digits) + "]"

        # Exported keys must be at least two digits and unique digits.
        # We will start 12 will be our first possiblility
        # !!!! Might be able to minimize loop by thinking about where the export key could really start !!!
        export_key = 10

        while export_key <= max_export_key:
            # When creating export keys our pairing_key must be in the number
            # Export keys will also have no repeating numbers so we test for that second
            if re.search(export_key_illegal_digits_regex, str(export_key)):
                export_key += 1
            else:
                if pairing_key == str(export_key)[0] and len(str(export_key)) == len(set(str(export_key))):
                    # The export value of the mapper is the pairing_left
                    export_value = pop_out_string(pop_out_this=export_key, original_string=pairing_left)

                    print((''.join(sorted(str(export_key)))) + '\t' + (''.join(sorted(str(export_value)))))
                    # Debug line that does not sort print(str(export_key) + '\t' + (''.join(sorted(str(export_value)))))
                export_key += 1



        line = sys.stdin.readline()



if __name__ == '__main__':
    main(sys.argv)