#!/bin/bash
python mapper2.py < input2.txt > intermediate2.txt
sort intermediate2.txt > intersorted2.txt
python reducer2.py < intersorted2.txt > output2.txt
