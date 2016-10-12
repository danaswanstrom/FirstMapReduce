#!/bin/bash
python mapper3.py < input3.txt > intermediate3.txt
sort intermediate3.txt > intersorted3.txt
python reducer3.py < intersorted3.txt > output3.txt
nano output3.txt
