import webbrowser
import os
import numpy as np
import datetime
import json

from Genetic_Distance_Calculation.kmedoid.k_medioid import kMedoids
from Genetic_Distance_Calculation.kmedoid.k_mer_to_distance_matrix import distanceMatrixGenerator

file_Path = "../kmer/kmer_similarity.txt"

data = distanceMatrixGenerator(file_Path)
data_label, distance_matrix = data[0], np.array(data[1])

data_label_copy = data[0].copy()

for i in range(0,5):
    for j in range(0,5):
        if(distance_matrix[i][j] == 0):
            distance_matrix[i][j] = 1000
        else:
            distance_matrix[i][j]=1000/distance_matrix[i][j]

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
        parentDict['children'] = [{'name': ''}, {'name': ''}]
        globalSpecieList.append([level,currentchildId1,new_specie_list_1])
        globalSpecieList.append([level,currentchildId2,new_specie_list_2])
        recursive(new_specie_list_1, distanceMatirixGenerator(data[1][0]), level,parentId+'1',parentDict['children'][0])
        recursive(new_specie_list_2, distanceMatirixGenerator(data[1][1]), level,parentId+'2',parentDict['children'][1])

# Begin Process
time = datetime.datetime.now()
parentDict = {'name':''}
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
    # print(e_l,temp)
    arranged_list.append(temp)

with open('kmer_tree.json','w') as outfile:
    json.dump(parentDict,outfile)
elapsed_time = datetime.datetime.now() - time

print("Json file created ..")

print("Elapsed Time in Mili sec :" , elapsed_time.total_seconds()*1000)

filename = os.getcwd()+'/' + 'Tree_visualization_kmer.html'
webbrowser.open_new_tab(filename)
