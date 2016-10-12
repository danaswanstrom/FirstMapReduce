import sys

current_combination = None
current_recommendation = '0123456789'
#test = ['12	345','12    35', '123	4', '123	4', '123	45', '123	45', '123   ']

for line in sys.stdin:
    line = line.strip()
    combination, recommendation = line.split('\t', 1)
    if current_combination == combination:
        current_recommendation = ''.join(sorted(set(recommendation) & set(current_recommendation)))
    else:
        if current_combination:
            # This test required because the mapper used 0 as the value for no recommendation. Output is to not print 0
            if current_recommendation == '0':
                current_recommendation = ''
            print(' '.join(current_combination) + ' : ' + ' '.join(current_recommendation))
        current_combination = combination
        current_recommendation = recommendation
if current_combination == combination:
    # This test required because the mapper used 0 as the value for no recommendation. Output is to not print 0
    if current_recommendation == '0':
        current_recommendation = ''
    print(' '.join(current_combination) + ' : ' + ' '.join(current_recommendation))