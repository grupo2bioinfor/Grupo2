# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:22:54 2019

@author: Angelica
"""


#Análise de homologias por BLAST

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO
from Bio import SeqIO
import re
#
#file1=open('gene.xls')
#lines=file1.readlines()
#
#file1.close()
##
#
#for i in range(len(lines)):
#    lines[i]=lines[i].split('\t')
#
#isoform='tuberin isoform 1'
#
#for i in range(len(lines)):
#    if lines[i][0]==isoform:
#        sequence=lines[i][5]






#
##        
##        
#fich=open('fstform.fasta', 'w')
#fich.write('>'+isoform+'\n'+sequence)
#
#fich.close()
##
#
#record = SeqIO.read("fstform.fasta", format="fasta")


##SeqIO lê em formato fasta
##
#result_handle = NCBIWWW.qblast("blastp", "swissprot", record) #o ultimo parametro, pondo a seq, tinha de estar em fasta para ser lido
#blastp para proteinas
#blastn para nucleotidos
#utilizou-se para proteinas porque caso se tenha verificado a troca de um nucleotido, o aminoacido pode ser o mm-redundancia dos aminoacidos
#utilizou-se a swissprot porque é uma fonte mais fidedigna
#
#file= open("my_blast.xml", "w")
##
#file.write(result_handle.read())
#    
#file.close()
#result_handle.close()

#Foi necessario criar um ficheiro com o blast para que este pudesse ser acedido mais que uma vez

#result_handle = open("my_blast.xml")
#
#blast_record = NCBIXML.parse(result_handle)
#
##
#arq=open('best_score.xml', 'w')
#e_value = 0.05
#
#for rec in blast_record:
#    for alignment in rec.alignments:
#        for hsp in alignment.hsps:
#            if hsp.expect < e_value:
#                arq.write('****Alignment****'+'\n'+'sequence:'+alignment.title+'\n'+
#                          'lenghth:'+ str(alignment.length)+'\n'+'e-value:'+ str(hsp.expect)+'\n'+
#                          hsp.query +'\n'+hsp.match +'\n'+
#                          hsp.sbjct +"\n"*2)
                          
#arq.close()


arq=open('best_score.xml','r')
lines = arq.readlines()
arq.close()

d={}
for i in range(len(lines)):
    if "AltName: Full=" in lines[i]:
        lines[i]=lines[i].split(';')
        for j in range(len(lines[i])):
            if ' AltName: Full=' in lines[i][j]:
                regex = 'Full=(.*)\['
                var=re.search(regex,lines[i][j]).group(1)
                if var in d:
                    d[var]+=1
                else:
                    d[var]=1

start=0
var=''
for i in d.keys():
    if d[i]>start:
        start=d[i]
        var=i
        
print(var)        