import sys
import re

def main(args):
    vowel_pattern = re.compile('[aeiouy]')
    pattern = re.compile('\S+')
    line = sys.stdin.readline()

    while line:
        for word in pattern.findall(line):
            print (str(len(vowel_pattern.findall(word))) + '\t' + '1')
        line = sys.stdin.readline()

if __name__ == '__main__':
    main(sys.argv)