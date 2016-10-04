import sys
import re

def main(argv):
    vowels = 'aeiou'
    line = sys.stdin.readln()
    pattern = re.compile('a-zA-Z0-9+')
    while line:
        for word in pattern.findall(line):
            print(len(findall('[%s]' % vowels, word) + '/t' + '1')
        line = sys.stdin.readln()

if __name__ == '__main__':
    main(sys.argv)