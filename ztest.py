import sys
import re

vowel_pattern = re.compile('[aeiou]')
pattern = re.compile('[a-zA-Z0-9]+')
p = re.compile('\d+')

line = sys.stdin.readline()
print (re.split('[\\s\\n]+', line))
while line:
	
    for word in pattern.findall(line):
        print (word + '\t' + str(len(vowel_pattern.findall(word))) + '\t' + '1')
       
    line = sys.stdin.readline()
