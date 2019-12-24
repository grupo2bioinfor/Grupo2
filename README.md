# Grupo2
# 
# A script "ncbi" contém uma função "literature_analysis" para obter literatura sobre cada um dos genes.
# Também estão disponíveis funções que acessam ao NCBI (get_nucleotide_files) e escrevem as features e anotações pretendidos num ficheiro xls (write_table). 
#
#A script "blast" utiliza as sequências obtidas para fazer um blast utilizando o qblast. A base de dados escolhida foi a SwissProt. Se um gene tiver mais de uma isoforma, apenas uma é escolhida para fazer o blast. Os resultados do blast são escritos num ficheiro xml, e são depois tratados de forma a escolher os melhores resultados (e-value<10^-35; score>130). Os melhores resultados são guardados num ficheiro xml e são tratados de forma a ser obtida a função das duas proteínas com base no BLAST.
#
#
#A script "phylogeny" utiliza os resultados do blast para selecionar um conjunto de sequências do mesmo gene pertencente a outros organismos e guarda-las num ficheiro em formato fasta. Este ficheiro será utilizado para fazer alinhamentos múltiplos e construir árvores filogenéticas. Estes dois ultimos passos são realizados manualmente utilizando o EMBL ou o MEGA-X software.
#
#
