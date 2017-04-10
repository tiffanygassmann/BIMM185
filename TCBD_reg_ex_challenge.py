# BIMM185-Week-1
Advanced Bioinformatics Labratory

import re

f_open = open('TCDB.faa')
f_read = f_open.read()

f_read = f_read.replace('\n', "") + '>'


line_1 = "\|[0-9a-zA-Z]+\|[0-9A-Z\.]+"
line_2  = "][A-Z]+>"
IDS = re.findall(line_1,f_read)

SEQS = re.findall(line_2, f_read)



length = len(SEQS)
expression = []

final = ""



with open('out_2.txt', 'w') as file:
    for x in xrange(length):
        expression = IDS[x].split("|")
        SEQ = SEQS[x].strip(">").strip("]")
        print >>file, expression[2] + " - " + expression[1] + "\t" + SEQ
