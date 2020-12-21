#!/usr/local/bin/python3
from docx2pdf import convert
import sys

if(len(sys.argv) != 3):
	print(f"{sys.argv[0]} <input file> <output file>")
	exit()

convert(sys.argv[1], sys.argv[2])
