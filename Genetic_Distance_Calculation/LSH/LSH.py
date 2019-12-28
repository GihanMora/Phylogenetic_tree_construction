import os
import time
from datasketch.minhash import MinHash
import concurrent.futures
import ast

from functools import reduce
filePath = "DNA_Sequences/"
splitValue = 200000
minHashPermmutations = 10

fileNameArray = []



dnaMinHashes = []


def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(set(list2))))
    union = len(set(list1).union(set(list2)))
    if(union == 0):
        return 0.0;
    else:
        return float(intersection / union)


def minHashing(splitedString):
    shringleLength = 5
    startIndex = 0
    m1 = MinHash(num_perm=minHashPermmutations)

    for x in range(0, int(round(len(splitedString) / shringleLength))):
        m1.update(splitedString[startIndex:(startIndex + shringleLength)].encode('utf8'))
        startIndex = startIndex + shringleLength;

    return m1.hashvalues

def LSH(filename):

    print ("task started "+ filename);

    taskStartTime = time.time()

    file1 = open(filePath + filename, "r")
    dnaSet1 = file1.read()
    flag = True
    startPointer = 0
    dnaLength = len(dnaSet1)
    # print(dnaLength)
    # print("dna length ",dnaLength)
    oneSpecyMinHash = []
    while (flag):

        if (startPointer + splitValue <= dnaLength):

            splitedString = dnaSet1[startPointer:startPointer + splitValue]
            minHashValue = minHashing(splitedString)
            oneSpecyMinHash+=list(minHashValue)
            startPointer = startPointer + splitValue

        else:

            splitedString = dnaSet1[startPointer::]
            minHashValue = minHashing(splitedString)
            oneSpecyMinHash+=list(minHashValue)
            flag = False

    onespecietoprint= [];

    onespecietoprint.append([filename,oneSpecyMinHash])

    f= open('specyhashes.txt', 'a+')
    f.writelines("%s\n" % item for item in onespecietoprint)
    f.close()

    print("time for " + filename + " minhashing", time.time() - taskStartTime)

    return oneSpecyMinHash;




def main():
    totStartTime = time.time();
    fileIndex = 1
    for filename in os.listdir(filePath):
        fileNameArray.append(filename)
        fileIndex += 1

    print(fileNameArray)

    with concurrent.futures.ProcessPoolExecutor(5) as executor:
        for filename, minhashArray in zip(fileNameArray, executor.map(LSH, fileNameArray)):

            dnaMinHashes.append([filename, minhashArray])

    print("total time = ", time.time()-totStartTime)
    fo= open('specyhashes.txt', 'r')
    f1 = fo.readlines()

    comparingStartTime = time.time();

    for i in range(0,len(f1)):
        for j in range (i,len(f1)):
            f_item_i = ast.literal_eval(f1[i])
            f_item_j = ast.literal_eval(f1[j])
            print("jaccard similarity between "+ f_item_i[0] +" and " + f_item_j[0] +" is : " ,jaccard_similarity(f_item_i[1], f_item_j[1]))
            f = open('LSH_similarity.txt', 'a+')
            f.writelines("%s\n" % (f_item_i[0][:-4] +","+ f_item_j[0][:-4]+","+ str(jaccard_similarity(f_item_i[1], f_item_j[1]))) )
            f.close()

    print ("time for comparing = ", time.time()-comparingStartTime)



if __name__ == '__main__':
    main()

