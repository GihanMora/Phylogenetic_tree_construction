import numpy as np
import datetime
# from nested_lookup import get_all_keys

from Plotting.Clustering.k_medioid import kMedoids

# # data_Labels
data_label = ['A', 'B', 'C',
              'D', 'E', 'F' ,
              'G' , 'H' , 'I']
#
# give distance matrix directly
distance_matrix = np.array(
[[0,0.010432221, 0.009252988, 0.016038109, 0.015792664, 0.015261977, 0.009469802,0.012129147,0.00933882],
                            [0.010432221, 0, 0.113680194, 0.159966678, 0.169917354, 0.138121955,0.182687492,0.111979141,0.183083489],
                            [0.009252988, 0.113680194, 0, 0.144963997, 0.158541919, 0.165510453,0.09513175,0.088293459,0.094672827],
                            [0.016038109, 0.159966678, 0.144963997, 0, 0.340560852, 0.301574262,0.167131109,0.113547955,0.165263827],
                            [0.015792664, 0.169917354, 0.158541919, 0.340560852, 0,0.344552414, 0.197706153,0.124429955,0.19602953],
                            [0.015261977, 0.138121955, 0.165510453, 0.301574262, 0.344552414, 0,0.196467151,0.12391129,0.196342867],
                            [0.009469802, 0.182687492, 0.09513175, 0.167131109, 0.344552414, 0.196467151,0,0.124647914,0.548456843],
                            [0.124647914, 0.12391129, 0.124429955, 0.113547955, 0.088293459, 0.111979141,0.012129147,0,0.124342619],
                            [0.00933882, 0.010432221, 0.094672827, 0.165263827, 0.19602953, 0.196342867,0.548456843,0.124342619,0]
                            ]
)

for i in range(0,9):
    for j in range(0,9):
        if(distance_matrix[i][j] == 0):
            distance_matrix[i][j] = 1000
        else:
            distance_matrix[i][j]=1/distance_matrix[i][j]

data_label_c_1 = ['A', 'B', 'C',
              'D', 'E', 'F' ,
              'G' , 'H' , 'I']

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
        parentDict['children'] = {"name": specieList[0]}
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
#
# def searchItems(gloat):
#     for level in gloat:
#         if (len(level) == 3):
#             key = level[1]
#             value = level[2]
#             count = 0
#             for j in range(0,len(key)-1):
#                 keyPrev = (key[0:j+1])
#                 print(dic["children"],"name")
#                 if(keyPrev in get_all_keys(dic["children"])):
#                     count=count+1
#
# specie_1_List = []
# specie_2_List = []
# finaDic = { 'name': '', 'children': [] }
#
# def constructDumyDic(specieList):
#     for level in specieList:
#         if(len(level) == 3):
#             key = level[1]
#             value = level[2]
#             if(key[0] == '1'):
#                 dicNew = {}
#                 dicNew["name"] = key
#                 dicNew["children"] = value
#                 specie_1_List.append(dicNew)
#             if (key[0] == '2'):
#                 dicNew = {}
#                 dicNew["name"] = key
#                 dicNew["children"] = value
#                 specie_2_List.append(dicNew)
#
# constructDumyDic(globalSpecieList)
#
# def searchDic(key, value, dictionary, x=1):
#     # First Character Actual string
#     tempKey = key[0:x]
#     print("Tempkey",tempKey)
#     print(dictionary)
#     count = 0
#     for i in dictionary['children']:
#         if isinstance(i,dict):
#             count+=1
#     print("count",count)
#     if (len(key)>=x and count >= 1):
#         print("RUNS THIS")
#         if(dictionary["children"][0]["name"] == tempKey):
#             print("FROM HERE")
#             x+=1
#             d = dictionary["children"][0]
#             searchDic(key,value,d,x)
#         else:
#             newDic = {}
#             print("adiing")
#             newDic["name"] = tempKey
#             newDic["children"]= []
#             tlist = []
#             tlist.append(newDic)
#             dictionary["children"] = tlist
#             d = dictionary["children"][-1]
#             print(dictionary)
#             searchDic(key, value, d, x + 1)
#
#     elif (len(key)>=x):
#         newDic = {}
#         print("adiing")
#         newDic["name"] = tempKey
#         newDic["children"] = []
#         newArray = []
#         newArray.append(newDic)
#         dictionary["children"]= newArray
#         d = dictionary["children"][-1]
#         print(dictionary)
#         searchDic(key, value, d, x + 1)
#
#
# dd =[
#   [1, '1', ['A', 'B', 'D', 'F', 'G']],
#   [1, '2', ['C', 'E', 'H', 'I']],
#   [2, '11', ['A', 'B', 'F', 'G']],
#   [2, '12', ['D']],
#   [3, '111', ['B']],
#   [3, '112', ['A', 'F', 'G']],
#
#   [4, '1121', ['F']],
#   [4, '1122', ['A', 'G']],
#
#   [5, '11221', ['G']],
#   [5, '11222', ['A']],
#
#   [2, '21', ['E', 'H']],
#   [2, '22', ['C', 'I']],
#   [3, '211', ['H']],
#   [3, '212', ['E']],
#
#   [3, '221', ['I']],
#   [3, '222', ['C']]]
# #
#
#
#
# # {'name': '', 'children': [{'name': '1', 'children': [{'name': '11', 'children': [{'name': '111', 'children': []}, {'name': '112', 'children': []}, {'name': '112', 'children': [{'name': '1121', 'children': []}]}, {'name': '112', 'children': [{'name': '1122', 'children': []}]}, {'name': '112', 'children': [{'name': '1122', 'children': [{'name': '11221', 'children': []}]}]}, {'name': '112', 'children': [{'name': '1122', 'children': [{'name': '11222', 'children': []}]}]}]}, {'name': '12', 'children': []}]}, {'name': '2', 'children': []}, {'name': ['B'], 'children': []}, {'name': ['F'], 'children': []}, {'name': ['G'], 'children': []}, {'name': ['A'], 'children': []}, {'name': ['D'], 'children': []}, {'name': '2', 'children': [{'name': '21', 'children': []}]}, {'name': '2', 'children': [{'name': '22', 'children': []}]}, {'name': '2', 'children': [{'name': '21', 'children': [{'name': '211', 'children': []}]}]}, {'name': '2', 'children': [{'name': '21', 'children': [{'name': '212', 'children': []}]}]}, {'name': ['H'], 'children': []}, {'name': ['E'], 'children': []}, {'name': '2', 'children': [{'name': '22', 'children': [{'name': '221', 'children': []}]}]}, {'name': '2', 'children': [{'name': '22', 'children': [{'name': '222', 'children': []}]}]}, {'name': ['I'], 'children': []}, {'name': ['C'], 'children': []}]}
#
# dic = {"name":"","children":[]}
#
# searchDic('1',[],dic,1)
# searchDic('2',['B'],dic,1)
# searchDic('11',[],dic,1)
# searchDic('12',[],dic,1)
# searchDic('111',[],dic,1)
# searchDic('112',[],dic,1)
# searchDic('1121',[],dic,1)
# #
# # for spe in specie_1_List:
# #     searchDic(spe[1],[],dic,1)
#
# print("ANS")
# print(dic)
