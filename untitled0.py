# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:34:20 2019

@author: emanuel
"""

from Bio import Entrez

Entrez.email = 'A.N.Other@example.com'

from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from re import search
from Bio import ExPASy
from Bio import SearchIO


#
#
#nucleotide_ids = ["NM_000548.5", "NM_001077183.2", "NM_001114382.2", "NM_001318827.1", "NM_001318829.1", 
#                  "NM_001318831.1", "NM_001318832.1", "NM_001363528.1", "NM_001370404.1", "NM_001370405.1",
#                  "NM_021055.2"]
#
#
#l=[]
##
#for nuc in nucleotide_ids:
#    hand = Entrez.efetch(db="nucleotide", id = nuc, rettype = "gb", rettmode = "text")
#    rec = SeqIO.read(hand,"genbank")
#    for feat in rec.features:
#        if feat.type== "CDS":
#            d={}
#            d['isoform']=''.join(str(e) for e in feat.qualifiers["product"][0:len(feat.qualifiers["product"])])
#            d['gene']=''.join(str(e) for e in feat.qualifiers['gene'][0:len(feat.qualifiers['gene'])])
#            d['note']=''.join(str(e) for e in feat.qualifiers['note'][0:len(feat.qualifiers['note'])])
#            d['codon_start']=''.join(str(e) for e in feat.qualifiers['codon_start'][0:len(feat.qualifiers['codon_start'])])
#            d['protein_id']=''.join(str(e) for e in feat.qualifiers['protein_id'][0:len(feat.qualifiers['protein_id'])])
#            d['translation']=''.join(str(e) for e in feat.qualifiers['translation'][0:len(feat.qualifiers['translation'])])
#        
#            l.append(d)
##        
#print(l)
#
#
    
file=open('gene.xls', 'w')

header = ["isoform","gene","note","codon_start","protein_id","translation","molecule_type","topology"]

for col in header:
    file.write(col+"\t")

file.write("\n")
for d in l:
    for value in d.values():
        file.write(str(value)+"\t")
    file.write("\n")
    
    
file.close()



#
#file = open("gene.xls")
#
#lines = file.readlines()
#
#file.close()
#
#for i in range(len(lines)):
#    lines[i] = lines[i].split("\t")
#    print(lines[i][0])




