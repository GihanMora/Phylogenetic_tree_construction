import numpy as np
import datetime
import json

from Genetic_Distance_Calculation.kmedoid.k_medioid import kMedoids
from Genetic_Distance_Calculation.kmedoid.k_mer_to_distance_matrix import distanceMatrixGenerator

file_Path = "/home/castle/repo/Phylogenetic_tree_construction/" \
            "Genetic_Distance_Calculation/kmedoid/kmer_result.txt"

data = distanceMatrixGenerator(file_Path)
data_label, distance_matrix = data[0], np.array(data[1])

data_label_copy = data[0].copy()
# data_label = ['A', 'B', 'C',
#               'D', 'E', 'F' ,
#               'G' , 'H' , 'I']
#
# give distance matrix directly
# distance_matrix = np.array(
# [[0,0.010432221, 0.009252988, 0.016038109, 0.015792664, 0.015261977, 0.009469802,0.012129147,0.00933882],
#                             [0.010432221, 0, 0.113680194, 0.159966678, 0.169917354, 0.138121955,0.182687492,0.111979141,0.183083489],
#                             [0.009252988, 0.113680194, 0, 0.144963997, 0.158541919, 0.165510453,0.09513175,0.088293459,0.094672827],
#                             [0.016038109, 0.159966678, 0.144963997, 0, 0.340560852, 0.301574262,0.167131109,0.113547955,0.165263827],
#                             [0.015792664, 0.169917354, 0.158541919, 0.340560852, 0,0.344552414, 0.197706153,0.124429955,0.19602953],
#                             [0.015261977, 0.138121955, 0.165510453, 0.301574262, 0.344552414, 0,0.196467151,0.12391129,0.196342867],
#                             [0.009469802, 0.182687492, 0.09513175, 0.167131109, 0.344552414, 0.196467151,0,0.124647914,0.548456843],
#                             [0.124647914, 0.12391129, 0.124429955, 0.113547955, 0.088293459, 0.111979141,0.012129147,0,0.124342619],
#                             [0.00933882, 0.010432221, 0.094672827, 0.165263827, 0.19602953, 0.196342867,0.548456843,0.124342619,0]
#                             ]
# )

for i in range(0,5):
    for j in range(0,5):
        if(distance_matrix[i][j] == 0):
            distance_matrix[i][j] = 1000
        else:
            distance_matrix[i][j]=1/distance_matrix[i][j]

data_label_c_1 = data_label_copy

def k_mediod_cluster(data_label_local, distance_matrix):
    M, C = kMedoids(distance_matrix, 2)
    clustered_species = []
    for each_key in C:
        temp = []
        for sp in C[each_key]:
            temp.append(data_label_local[sp])
        clustered_species.append(temp)

    clustered_indexes = []
    for each_key in C:
        temp = []
        for sp in C[each_key]:
            temp.append(sp)
        clustered_indexes.append(temp)

    return [clustered_species,clustered_indexes]

def distanceMatirixGenerator(data_label_array):

    array_C_0=[]
    for i in data_label_array:
        label = data_label_c_1[i]
        array_C_0.append(data_label_c_1[list(data_label_c_1).index(label)])

    array = []
    array_row =[]
    for i in range(0,len(data_label_array)):
        array_row.append(0)
    for i in range(0, len(data_label_array)):
        array.append(array_row)
    array = np.array(array)
    for i in range(0, len(data_label_array)):
        for j in range(0, len(data_label_array)):
            array[i][j] = distance_matrix[data_label_array[i]][data_label_array[j]]

    return array


globalSpecieList = []

def recursive(specieList , disMat,level,parentId,parentDict):
    level+=1

    if len(specieList)==1:
        globalSpecieList.append([level,specieList])
        parentDict['name']=specieList[0]
        return specieList
    else:
        data = k_mediod_cluster(specieList, disMat)
        new_specie_list_1 , new_specie_list_2 = data[0][0],data[0][1]

        currentchildId1,currentchildId2= parentId+'1',parentId+'2'
        parentDict['children'] = [{'name': currentchildId1}, {'name': currentchildId2}]
        globalSpecieList.append([level,currentchildId1,new_specie_list_1])
        globalSpecieList.append([level,currentchildId2,new_specie_list_2])
        recursive(new_specie_list_1, distanceMatirixGenerator(data[1][0]), level,parentId+'1',parentDict['children'][0])
        recursive(new_specie_list_2, distanceMatirixGenerator(data[1][1]), level,parentId+'2',parentDict['children'][1])

# Begin Process
time = datetime.datetime.now()
parentDict = {'name':'0'}
recursive(data_label,distance_matrix,0,"",parentDict)
levels = []
for each_v in globalSpecieList:
    levels.append(each_v[0])
levels = set(levels)
arranged_list=[]
tempList = []

for e_l in levels:
    temp = []
    for each in globalSpecieList:
        if(each[0])==e_l:
            temp.append(each[1])
    print(e_l,temp)
    arranged_list.append(temp)

print(globalSpecieList)

# End Process
elapsed_time = datetime.datetime.now() - time

# Milliseconds
print("Elapsed Time in Mili sec :" , elapsed_time.total_seconds()*1000)
print(parentDict)
with open('sex.json','w') as outfile:
    json.dump(parentDict,outfile)
