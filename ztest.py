import sys
import re

vowel_pattern = re.compile('[aeiou]')
pattern = re.compile('\S+')
line = sys.stdin.readline()

while line:
	for word in pattern.findall(line):
        print (word + '\t' + str(len(vowel_pattern.findall(word))) + '\t' + '1')
    line = sys.stdin.readline()
