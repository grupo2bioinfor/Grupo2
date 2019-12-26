# -*- coding: utf-8 -*-


#Análise de homologias por BLAST

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO
from Bio import SeqIO
from re import *

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
result_handle = NCBIWWW.qblast("blastp", "swissprot", record.format("fasta")) #o ultimo parametro, pondo a seq, tinha de estar em fasta para ser lido
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

arq=open('best_score2.xml','r')     #procura a função e guarda num dicionário, em que a key é cada função presente no blast,
lines = arq.readlines()                 #e o valor é o número de vezes que essa função aparece
arq.close()
   
d={}
                                  #try para caso não exista "RecName" num dos 
for i in range(len(lines)):         #percorre todas as linhas do ficheiro
    if "RecName: Full=" in lines[i]:        #se uma linha tiver a função - nome da proteína (RecName)
        lines[i]=lines[i].split(';')        #transformar essa linha numa lista
        for j in range(len(lines[i])):
            if ' RecName: Full=' in lines[i][j]:        #usar search para encontrar o RecName
                regex = 'Full=(.*)'
                var=re.search(regex,lines[i][j]).group(1)
                if var in d:                #cada função será uma chave do dicionário; o seu valor é o número de vezes que aparece
                    d[var]+=1
                else:
                    d[var]=1

start=0
var=''
for i in d.keys():                      #procurar a função que aparece mais vezes
    if d[i]>start:
        start=d[i]
        var=i
print(d)
print("----------")
print(var)   


