import sys, bz2
from collections import defaultdict

def readfile():
        file = bz2.BZ2File("RS.txt.bz2")
        contents = file.readlines()

        proteins = defaultdict(list)

        counter = 0
        max_proteins = 2000

        for line in contents:

                info = line.split('\t')

                ID = info[0]
                ID2 = (info[1],info[3].rstrip("\n"))

                #first 2000
                if ID not in proteins:
                    counter +=1
                    if counter > max_proteins:
                        break
                #add items to dictionary
                proteins[ID].append(ID2)
        return proteins

def compare_proteins(proteins):

        best_matches = []
        max_length = 0
        max_protein = ''

        for protein in proteins.keys():
            #proteins[key] list of tuples, second item of tuple
            res = max(proteins[protein], key = lambda x:x[1])
            best_matches.append((protein,res))

            length = len(proteins[protein])

            if length > max_length:
                max_length = length
                max_protein = protein

        return best_matches, max_protein, max_length

#output

proteins = readfile()
p_list,max_p,max_l = compare_proteins(proteins)

with open('out.txt', 'w') as file:
    print >> file, ((max_p,max_l))
    for item in p_list:
        print>>file, item
