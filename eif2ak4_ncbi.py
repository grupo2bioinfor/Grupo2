# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:05:12 2019

@author: Angelica
"""

#; Análise de literatura; análise da sequência e das features presentes no NCBI  


#
import csv
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "A.N.Other@example.com" 
handle = Entrez.esearch(db='pubmed', term='EIF2AK4')
record = Entrez.read(handle) #o read da acesso aos artigos de forma ordenada
handle.close()
print(record)
#efetch faz download de um record
#esearch faz uma pesquisa
##aceder ao ncbi
#

nucleotide_ids = ["NM_001013703.4"]
l=[]
for i in nucleotide_ids:
    handle = Entrez.efetch(db="nucleotide", id=i, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
#    
    d={}
    for feat in record.features:
       feat_types.append(str(feat.type))
       feat_locations.append(str(feat.location))
       if feat.type=='CDS':    #CDS para obter a coding sequence
           key_list=['product', 'gene', 'note', 'codon_start','protein_id','translation']
           for key in key_list:
               d[key]= ''.join(feat.qualifiers[key])
    d["Features"] = ', '.join(feat_types)
    d["Feature locations"] = ', '.join(feat_locations)
    keys_annot=['molecule_type','topology','organism','taxonomy','comment']
    for key in keys_annot:
        if key=='comment':
            d[key]=record.annotations[key].replace('\n', ' ')
        else:
            d[key]=record.annotations[key]
    
    l.append(d)
print(l)

#
## do gene
#
##
##
#
#    
file=open('gene2.xls', 'w')
header=['isoform', 'gene', 'note', 'codon_start','protein_id','translation', "Features", 
            "Feature location", 'molecule_type',
        'topology','organism','taxonomy','comment']
for col in header:
    file.write(col+'\t')
file.write('\n')
    
for d in l:
    for value in d.values():
        file.write(str(value) + "\t")
    file.write('\n')
file.close()
