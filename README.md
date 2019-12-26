# Grupo2
# 
# Este ficheiro contém uma descrição das scrips desenvolvidas. Cada script foi duplicada para cada gene, com as alterações necessárias.
#
#As scripts "tsc2_ncbi" e "eif2ak4_ncbi" contém uma código para obter literatura sobre cada um dos genes.
Também está disponível código que acede ao NCBI e escreve as features e anotações pretendidos num ficheiro xls. 
#
#
#As script "tsc2_blast" e "eif2ak4_blast" utilizam as sequências obtidas para fazer um blast utilizando o qblast. A base de dados escolhida foi a SwissProt. Se um gene tiver mais de uma isoforma, apenas uma é escolhida para fazer o blast. Os resultados do blast são escritos num ficheiro xml, e são depois tratados de forma a escolher os melhores resultados (e-value<10^-35; score>130). Os melhores resultados são guardados num ficheiro xml e são tratados de forma a ser obtida a função das duas proteínas com base no BLAST.
#
#
#As scripts "tsc2_phylogeny" e "eif2ak4_phylogeny" utilizam os resultados dos blast para selecionar um conjunto de sequências do mesmo gene pertencente a outros organismos e guarda-las num ficheiro em formato fasta. Este ficheiro será utilizado para fazer alinhamentos múltiplos e construir árvores filogenéticas. Estes dois ultimos passos são realizados manualmente utilizando o EMBL ou o MEGA-X software.
#
#
