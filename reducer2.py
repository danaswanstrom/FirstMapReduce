import sys

current_vowel_str = None
current_count = 0
vowel_str = None
#test = ['ae	1', 'ae	1','io	1','io	1','io	1','y	1','y	1', 'y	1', 'y	1']

for line in sys.stdin:
    line = line.strip()
    vowel_str, count = line.split('\t', 1)
    count = int(count)


    if current_vowel_str == vowel_str:
        current_count += count

    else:

        if current_vowel_str:
            if current_vowel_str == '_':
                current_vowel_str = ' '
            print('%s\t%s' % (current_vowel_str, current_count))
        current_count = count
        current_vowel_str = vowel_str

if current_vowel_str == vowel_str:
    if current_vowel_str == '_':
        current_vowel_str = ' '
    print('%s\t%s' % (current_vowel_str, current_count))