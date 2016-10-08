import sys
import re

vowels = 'aeiou'
line = sys.stdin.readline()
pattern = re.compile('[a-zA-Z0-9]+')
p = re.compile('\d+')
while line:
    for word in pattern.findall(line):
        print (word + '\t' + str(len(word)) + '\t' + '1')
    line = sys.stdin.readline()
