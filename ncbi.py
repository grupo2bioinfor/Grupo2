# -*- coding: utf-8 -*-


"""
Created on Tue Nov 26 11:22:54 2019
@author: Angelica
"""


#Análise de literatura
#Análise da sequência e das features presentes no NCBI


from Bio import SeqIO
from Bio import Entrez
Entrez.email = "A.N.Other@example.com"  # Always tell NCBI who you are


def literature_analysis(search_term):
    handle = Entrez.esearch(db='pubmed', term=search_term) #faz pesquisa na base de dados do NCBI PubMed
    record = Entrez.read(handle) #o read lê os artigos de forma ordenada
    handle.close()
    print(record)               #faz print dos resultados obtidos



def get_nucleotide_files(nucleotide_ids):
    #retorna uma lista (l) em que os elementos são dicionários. Cada dicionário tem informação para uma isoforma
    
    l=[]            #lista onde serão guardadas as informações de todas as isoformas
    for i in nucleotide_ids:            # para cada isoforma, é acessado o record presente na base de dados "nucleotide" do ncbi
        handle = Entrez.efetch(db="nucleotide", id=i, rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")      #ler a informação obtida
        handle.close()      
        d={}                        #guardar a informação relevante num dicionário 
        for feat in record.features:    #percorrer as features de cada isoforma
          if feat.type=='CDS':    #CDS para obter a coding sequence
              key_list=['product', 'gene', 'note', 'codon_start','protein_id','translation']  #lista de features consideradas relevantes
              for key in key_list:
                  d[key]= ''.join(feat.qualifiers[key])
        keys_annot=['molecule_type','topology','organism','taxonomy','comment']  #lista de anotaçoes consideradas relevantes
        for key in keys_annot:
            if key=='comment':              #nas anotações "comment" há '\n' que fazem o texto mudar de linha
                d[key]=record.annotations[key].replace('\n', ' ')
            else:
                d[key]=record.annotations[key]
        
        l.append(d)
    return l
    

def write_table(l, file_name):
    file=open(file_name + '.xls', 'w')                 #abrir ficheiro .xls (Excel)
    header=['isoform', 'gene', 'note', 'codon_start','protein_id','translation','molecule_type',    
            'topology','organism','taxonomy','comment']         # nomes do cabeçalho das colunas
    for col in header:              #escrever o cabeçalho no ficheiro
        file.write(col+'\t')        # o '\t' serve para mudar de célula na folha de Excel
    file.write('\n')
    for d in l:                     #para cada isoforma, são guardados no ficheiro os valores das features e anotações 
        for value in d.values():        #guardadas anteriormente em dicionários
            file.write(str(value) + "\t")
        file.write('\n')
    file.close()
    
    
    
    
def test():
    literature_analysis("TSC complex subunit 2")     #pesquisa de literatur sobre TSC2
    literature_analysis("EIF2AK4")                   #pesquisa de literatura sobre EIF2AK4
          
    nucleotide_ids_tsc2 = ["NM_000548.5", "NM_001077183.2", "NM_001114382.2", "NM_001318827.1", "NM_001318829.1", 
                      "NM_001318831.1", "NM_001318832.1", "NM_001363528.1", "NM_001370404.1", "NM_001370405.1",
                      "NM_021055.2"]
    
    nucleotide_ids_eif2ak4=["NM_001013703.4"]
    
    ###os nucleotide_ids são os ids de cada isoforma de cada gene
    
    l1=get_nucleotide_files(nucleotide_ids_tsc2)    #retorna uma lista com informação sobre o gene TSC2
    l2=get_nucleotide_files(nucleotide_ids_eif2ak4) #retorna uma lista com informação sobre o gene EIF2AK4
    write_table(l1, "gene")                                 #escreve os resultados obtidos num excel, para cada gene; 
    write_table(l2, "gene1")                                 # "gene" é o nome do ficheiro para o TSC2, e "gene1" para o EIF2AK4

test()
