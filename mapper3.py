import sys
import re

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
        pairing_left_regex = "[" + pairing_left + "]"

        # Length of digits will determine max length of exported key
        # Max export key will be all 9's and the same length. Max as a int
        digits_len = len(pairing_digits)
        max_export_key = int('9' * digits_len)

        # Exported keys must be at least two digits and unique digits.
        # We will start 12 will be our first possiblility
        # !!!! Might be able to minimize loop by thinking about where the export key could really start !!!
        export_key = 12
        line = sys.stdin.readline()

        

if __name__ == '__main__':
    main(sys.argv)