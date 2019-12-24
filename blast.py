# -*- coding: utf-8 -*-

"""
Created on Tue Nov 26 11:25:30 2019
@author: Angelica
"""

#Análise de homologias por BLAST

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import re
#


def write_fasta(excel, isoform ,fasta):        #abre o excel criado no módulo "ncbi", e escreve a sequencia de uma isoforma (isoform),
    file1=open(excel + '.xls')                 #em formato fasta 
    lines=file1.readlines()    
    file1.close()
    
    for i in range(len(lines)):
        lines[i]=lines[i].split('\t')
    
    
    for i in range(len(lines)):
        if lines[i][0]==isoform:
            sequence=lines[i][5]
   
       
    fich=open(fasta+'.fasta', 'w')
    fich.write('>'+isoform+'\n'+sequence)
    
    fich.close()


def blast(fasta_name, blast_file):                      #função que faz o blast, lendo um ficheiro fasta, e escreve os resultados num ficheiro xml
    record = SeqIO.read(open("fstform2.fasta"), format="fasta")                #SeqIO lê em formato fasta
    result_handle = NCBIWWW.qblast("blastp", "swissprot", record.format("fasta"))
    #o ultimo parametro, pondo a seq, tem de estar em fasta para ser lido
    # blastp para proteinas
    # blastn para nucleotidos
    # utilizou-se para proteinas porque caso se tenha verificado a troca de um nucleotido, o aminoacido pode ser o mm-redundancia dos aminoacidos
    # utilizou-se a swissprot porque é uma fonte mais fidedigna, contendo apenas records revistos manualmente

    print('BLAST finished')             #confirmar que o blast acabou

    file= open(blast_file + ".xml", "w")   # Foi necessario criar um ficheiro com o blast para que este pudesse ser acedido mais que uma vez
    file.write(result_handle.read())      
    file.close()
    result_handle.close()


def best_results(blast_results, best_results):     #função que seleciona apenas os melhores resultados do blast: e-value menor que 10^-35
    result_handle = open(blast_results + ".xml")    #blast results é o nome do ficheiro com os resultados do blast
    blast_record = NCBIXML.read(result_handle)      
    result_handle.close()
    arq=open(best_results + '.xml', 'w')            #best_results é o nome do ficheiro com os melhores resultados
    e_value = 10**(-35)            
                 #e-value máximo aceitado
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < e_value and hsp.score > 130:   #selecionar resultados com e-value menor que 10^-35 e score maior que 130
                arq.write('****Alignment****'+'\n'+'sequence:'+alignment.title+'\n'+
                          'lenghth:'+ str(alignment.length)+'\n'+'e-value:'+ str(hsp.expect)+'\n'+
                          hsp.query +'\n'+hsp.match +'\n'+
                          hsp.sbjct +"\n"*2)
                              
    arq.close()



def get_function(best_results):             #função que procura atribuir uma função a uma proteína com base nos resultados do blast
    arq=open(best_results + '.xml','r')     #procura a função e guarda num dicionário, em que a key é cada função presente no blast,
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
    print(var)                          #faz print da função obtida


def test():
    write_fasta("gene", 'tuberin isoform 1', "fstform")         #criar fasta com sequencia da isoforma 1 do TSC2
    write_fasta("gene1", "eIF-2-alpha kinase GCN2", "fstform2") #criar fasta com sequencia de EIF2AK4
    blast("fstform", "my_blast")
    blast("fstform2", "my_blast2")
    best_results("my_blast", "best_score")
    best_results("my_blast1", "best_score2")
    get_function("best_score2")
    
test()



