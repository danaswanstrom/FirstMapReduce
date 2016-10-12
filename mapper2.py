import sys
import re

def main(args):
    vowel_pattern = re.compile('[aeiouyAEIOUY]+')
    pattern = re.compile('\S+')
    line = sys.stdin.readline()

    while line:
        for word in pattern.findall(line):
            all_vowels_str = ''.join(vowel_pattern.findall(word))
            all_vowels_str = all_vowels_str.lower()
            if all_vowels_str == '':
                all_vowels_str = '_'
            print (str(''.join(sorted(all_vowels_str))) + '\t' + '1')
        line = sys.stdin.readline()

if __name__ == '__main__':
    main(sys.argv)