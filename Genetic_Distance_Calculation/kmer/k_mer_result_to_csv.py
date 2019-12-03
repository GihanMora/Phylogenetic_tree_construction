import pandas as pd

filePath = "/home/castle/Desktop/Phylogenetic_tree_construction/" \
           "Genetic_Distance_Calculation/kmer/kmer_similarity.txt"

num_of_species = 6

specie_names = []

with open(filePath) as f:
    first_line = f.readline()
    content = f.read()
    for i in range(0,num_of_species):
        specie_names.append(content.split("\n")[1])

    for specie_name in specie_names:


    f.close()




print(specie_names)
