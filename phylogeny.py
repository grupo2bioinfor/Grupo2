# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:54:54 2019

@author: emanuel
"""

from Bio import Phylo
from Bio import ExPASy
from Bio import SwissProt



def get_sequence(best_results, fasta_name):  #função que procura as sequencias dos resultados do blast na UniProt, e guarda-as em fasta                
    file = open(best_results + ".xml")       #abrir ficheiro com melhores resultados do blast
    lines = file.readlines()
    file.close()   
    l=[]
       
    for i in range(len(lines)):              # o id encontra-se a seguir a "sequence:sp|"
        if "sequence:sp" in lines[i]:
            lines[i] = lines[i].split("|")
            l.append(lines[i][1])
    d={}                                #guardar a informação num dicionário: nome da espécie são as chaves e a sequencia são os valores
    for i in l:      
        try:                            #try para garantir que o acesso à UniProt correu bem
            handle = ExPASy.get_sprot_raw(i)
            record = SwissProt.read(handle)
        except Exception as e:
            print(i,e)
        if record.organism not in d.keys():     #para casos em que o mesmo organism aparece mais que uma vez no resultado do blast,
            d[record.organism.upper()] = record.sequence  #guardamos apenas o primeiro;
       
    seqs_file = open("seqs.fasta","w")      #guardar as sequencias num fasta    
    for key in d.keys():
        seqs_file.write(">" + key + "\n" + d[key] + "\n\n")
     
    seqs_file.close()



def test():
    get_sequence("best_score", "seqs")
    get_sequence("best_score2", "seqs2")
    
    
test()

