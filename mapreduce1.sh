#!/bin/bash
python mapper1.py < input1.txt > intermediate1.txt
sort intermediate1.txt > intersorted1.txt
python reducer1.py < intersorted1.txt > output1.txt
nano output1.txt