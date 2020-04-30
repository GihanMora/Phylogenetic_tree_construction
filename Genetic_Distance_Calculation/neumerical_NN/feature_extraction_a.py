import ast
import os
import numpy as np

kmer_forests_path = "/home/castle/repo/Phylogenetic_tree_construction/Genetic_Distance_Calculation/kmer/kmer_forests/"
extracted_features_path = "/home/castle/repo/Phylogenetic_tree_construction/Genetic_Distance_Calculation/neumerical_NN/extracted_features/"


forest_list = os.listdir(kmer_forests_path)
# print(forest_list)

def nested_ACTG_counting(val, nesting = 0):
    if type(val) == dict:
        nesting += 1
        for k in val:
            # print(k,nesting)
            if k=='A':
                nested_count_containers[nesting - 1][0]+=1
            if k=='C':
                nested_count_containers[nesting - 1][1]+=1
            if k=='T':
                nested_count_containers[nesting - 1][2]+=1
            if k=='G':
                nested_count_containers[nesting - 1][3]+=1
            nested_ACTG_counting(val[k], nesting)
    else:

        print(val,nesting)


for each_forest in forest_list:

    #do this initialization suitable to the depth you want
    nested_count_containers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                               [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    print(each_forest)
    file = open(kmer_forests_path+each_forest,"r")
    forest_txt = file.read()
    forest = ast.literal_eval(forest_txt)

    nested_ACTG_counting(forest)
    new_text = open(extracted_features_path+each_forest,'w')
    new_text.write(str(nested_count_containers))
    new_text.close()
    # print(char_of_forest)


