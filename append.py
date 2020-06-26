import os
from PyPDF2 import PdfFileMerger

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

merger = PdfFileMerger()
f = open('list.txt','r')
for line in f:
	merger.append(line.strip())
	print(bcolors.OKGREEN + 'appended' + ' ' + line.strip() + bcolors.ENDC)
merger.write('output.pdf')
merger.close()