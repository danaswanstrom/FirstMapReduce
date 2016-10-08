import sys
import re

vowels = 'aeiou'
line = sys.stdin.readline()
pattern = re.compile('a-z+')
p = re.compile('\d+')
numbers = p.findall(line)

words = pattern.findall(line)
#words = line.split()
print (words)
print (numbers)
print (line)

#print ('Wordcount:')
#print  (wordcount)