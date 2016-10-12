import sys

current_combination = None
current_recommendation = '0123456789'

for line in sys.stdin:
    line = '12	345' #line.strip()
    combination, recommendation = line.split('\t', 1)
    if current_combination == combination:
        current_recommendation = ''.join(sorted(set(recommendation) & set(current_recommendation)))
    else:
        if current_combination:
            print(current_combination + '\t' + current_recommendation)
            current_combination = combination
            current_recommendation = recommendation
    if current_combination == combination:
        print(current_combination + '\t' + current_recommendation)