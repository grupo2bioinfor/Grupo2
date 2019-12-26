# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:20:59 2019

@author: Angelica
"""

#Análise de homologias por BLAST

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO
from Bio import SeqIO


file1=open('gene2.xls')
lines=file1.readlines()
#
file1.close()
##
#
for i in range(len(lines)):
    lines[i]=lines[i].split('\t')
#
isoform='eIF-2-alpha kinase GCN2'
#
for i in range(len(lines)):
    if lines[i][0]==isoform:
        sequence=lines[i][5]
#
#
##        
##        
fich=open('fstform2.fasta', 'w')
fich.write('>'+isoform+'\n'+sequence)
#
fich.close()
##
#
record = SeqIO.read("fstform2.fasta", format="fasta")


##SeqIO lê em formato fasta
##
result_handle = NCBIWWW.qblast("blastp", "swissprot", record) #o ultimo parametro, pondo a seq, tinha de estar em fasta para ser lido
##blastp para proteinas
##blastn para nucleotidos
##utilizou-se para proteinas porque caso se tenha verificado a troca de um nucleotido, o aminoacido pode ser o mm-redundancia dos aminoacidos
##utilizou-se a swissprot porque é uma fonte mais fidedigna
##
file= open("my_blast2.xml", "w")
##
file.write(result_handle.read())
##    
file.close()
result_handle.close()


#Foi necessario criar um ficheiro com o blast para que este pudesse ser acedido mais que uma vez
#
result_handle = open("my_blast2.xml")

blast_record = NCBIXML.parse(result_handle)

#
arq=open('best_score2.xml', 'w')
e_value = 10**(-35)

for rec in blast_record:
    for alignment in rec.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < e_value and hsp.score > 130:
                arq.write('****Alignment****'+'\n'+'sequence:'+alignment.title+'\n'+
                          'lenghth:'+ str(alignment.length)+'\n'+'e-value:'+ str(hsp.expect)+'\n'+
                          hsp.query +'\n'+hsp.match +'\n'+
                          hsp.sbjct +"\n"*2)
                          
arq.close()


