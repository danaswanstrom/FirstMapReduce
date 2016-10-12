#!/bin/bash
python mapper3.py < input3a.txt > intermediate3a.txt
sort intermediate3a.txt > intersorted3a.txt
python reducer3a.py < intersorted3a.txt > output3a.txt
nano output3a.txt
