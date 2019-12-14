
#Análise da sequência e das features presentes no NCBI  ; Análise de literatura


#
import csv
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are
#handle = Entrez.esearch(db='pubmed', term='TSC complex subunit 2') #a pubmed é uma base de dados de art ncbi
#record = Entrez.read(handle) #o read da acesso aos artigos de forma ordenada
#handle.close()
#print(record)
#efetch faz download de um record
#esearch faz uma pesquisa
#
##aceder ao ncbi
#

#nucleotide_ids = ["NM_000548.5", "NM_001077183.2", "NM_001114382.2", "NM_001318827.1", "NM_001318829.1", 
#                  "NM_001318831.1", "NM_001318832.1", "NM_001363528.1", "NM_001370404.1", "NM_001370405.1",
#                  "NM_021055.2"]
#l=[]
#for i in nucleotide_ids:
#    handle = Entrez.efetch(db="nucleotide", id=i, rettype="gb", retmode="text")
#    record = SeqIO.read(handle, "genbank")
#    handle.close()
#    
#    d={}
#    for feat in record.features:
#       if feat.type=='CDS':    #CDS para obter a coding sequence
#           key_list=['product', 'gene', 'note', 'codon_start','protein_id','translation']
#           for key in key_list:
#               d[key]= ''.join(feat.qualifiers[key])
#    keys_annot=['molecule_type','topology','organism','taxonomy','comment']
#    for key in keys_annot:
#        if key=='comment':
#            d[key]=record.annotations[key].replace('\n', ' ')
#        else:
#            d[key]=record.annotations[key]
#    
#    l.append(d)
#print(l)
##
#
## do gene
#
##
##
#
#    
file=open('gene1.xls', 'w')
header=['isoform', 'gene', 'note', 'codon_start','protein_id','translation','molecule_type',
        'topology','organism','taxonomy','comment']
for col in header:
    file.write(col+'\t')
file.write('\n')
    
for d in l:
    for value in d.values():
        file.write(str(value) + "\t")
    file.write('\n')
file.close()
###    
#
#
#
