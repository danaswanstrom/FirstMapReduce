import sys

current_vowel_num = None
current_count = 0
vowel_num = None
# test = ['0	1', '0	1','0	1','1	1','1	1','2	1','2	1', '2	1', '2	1']

for line in sys.stdin:
    line = line.strip()
    vowel_num, count = line.split('\t', 1)
    count = int(count)


    if current_vowel_num == vowel_num:
        current_count += count

    else:

        if current_vowel_num:
            print('%s\t%s' % (current_vowel_num, current_count))
        current_count = count
        current_vowel_num = vowel_num

if current_vowel_num == vowel_num:
    print('%s\t%s' % (current_vowel_num, current_count))