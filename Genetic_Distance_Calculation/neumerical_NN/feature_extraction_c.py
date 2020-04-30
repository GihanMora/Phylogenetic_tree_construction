import os
import time
from datasketch.minhash import MinHash
import concurrent.futures
import ast
from xlwt import Workbook
import csv
import pandas as pd
from functools import reduce
filePath = "sample_sequences/"
kmerACTGFilePath = 'extracted_features/'
ACTGcountFile = 'ACTGcount.txt'
new_specie_file = 'Acetobacter_pasteurianus_IFO_3283_26_uid158531_NC_017130.fna'




def compareKmerACTG(filename1, filename2):

    kmerDiffArray = []
    file1 = open(kmerACTGFilePath + filename1[:-4]+'.txt','r')
    kmer1Array = ast.literal_eval(file1.read())

    file2 = open(kmerACTGFilePath + filename2[:-4]+'.txt','r')
    kmer2Array = ast.literal_eval(file2.read())

    print(type(kmer2Array))
    kmerDiffA = 0;
    kmerDiffC = 0;
    kmerDiffT = 0;
    kmerDiffG = 0;
    for i in range (0,len(kmer2Array)):


        kmerDiffA = abs(kmer1Array[i][0]-kmer2Array[i][0])
        kmerDiffC = abs(kmer1Array[i][1] - kmer2Array[i][1])
        kmerDiffT = abs(kmer1Array[i][2] - kmer2Array[i][2])
        kmerDiffG = abs(kmer1Array[i][3] - kmer2Array[i][3])

        kmerDiffArray.append([kmerDiffA,kmerDiffC,kmerDiffT,kmerDiffG])

    return kmerDiffArray

def compareACTGtext(filename1, filename2):
    openFile = open(ACTGcountFile, 'r')
    data = openFile.read()

    countArray = ast.literal_eval(data)
    diffArray1 = []
    diffArray2 = []

    for specy in countArray:
        print(specy[0],filename1,filename2)
        if(specy[0]== filename1):
            diffArray1 = specy[1]

        elif(specy[0]==filename2):
            diffArray2 = specy[1]

    openFile.close()
    print(diffArray1,diffArray2)
    diffA = diffArray1[0] - diffArray2[0]
    diffC = diffArray1[1] - diffArray2[1]
    diffT = diffArray1[2] - diffArray2[2]
    diffG = diffArray1[3] - diffArray2[3]

    return ([abs(diffA), abs(diffC), abs(diffT), abs(diffG)])



def main():
    totStartTime = time.time();
    fileIndex = 1
    fileNameArray = []
    for filename in os.listdir(filePath):
        if filename != new_specie_file:
            fileNameArray.append(filename)
            fileIndex += 1

    print(fileNameArray)


    print("total time = ", time.time()-totStartTime)
    # fo= open('specyhashes.txt', 'r')
    # f1 = fo.readlines()

    fo = open('ACTGcount.txt', 'r')
    f1 = fo.readlines()


    comparingStartTime = time.time();
    wb = Workbook()
    sheet1 = wb.add_sheet('Attributes')
    sheet1.write(0,0, 'DNA 1')
    sheet1.write(0, 1, 'DNA 2')
    # sheet1.write(0, 2, 'LSH Similarity')
    sheet1.write(0, 2, 'Diff A')
    sheet1.write(0, 3, 'Diff C')
    sheet1.write(0, 4, 'Diff T')
    sheet1.write(0, 5, 'Diff G')
    # sheet1.write(0, 7, 'level1_Diff A')
    # sheet1.write(0, 8, 'level1_Diff C')
    # sheet1.write(0, 9, 'level1_Diff T')
    # sheet1.write(0, 10, 'level1_Diff G')


    sheet1Row = 1

    for i in range(0,len(fileNameArray)):
        f_item_j = fileNameArray[i]#ast.literal_eval(f1[i])
        f_item_i = new_specie_file#ast.literal_eval(f1[j])
        print(f_item_i,f_item_j)
        # print("jaccard similarity between "+ f_item_i[0] +" and " + f_item_j[0] +"is : " ,jaccard_similarity(f_item_i[1], f_item_j[1]))

        actgDiffs = compareACTGtext(f_item_i, f_item_j)
        print(actgDiffs)
        sheet1.write(sheet1Row, 0, f_item_i)
        sheet1.write(sheet1Row, 1, f_item_j)
        # sheet1.write(sheet1Row, 2, 404)
        sheet1.write(sheet1Row, 2, actgDiffs[0])
        sheet1.write(sheet1Row, 3, actgDiffs[1])
        sheet1.write(sheet1Row, 4, actgDiffs[2])
        sheet1.write(sheet1Row, 5, actgDiffs[3])


        kmerDifferences = compareKmerACTG(f_item_i,f_item_j)
        # diffs = []
        kmerDiffPrintColumn = 6
        for level in kmerDifferences[3:-2]:#skipping first three levels
            for diff in level:
                # diffs.append(diff)
                sheet1.write(sheet1Row,kmerDiffPrintColumn,diff)

                kmerDiffPrintColumn = kmerDiffPrintColumn+1
            #
            # kmerDistance = getKmerDistance(f_item_i[0], f_item_j[0])
            # sheet1.write(sheet1Row, kmerDiffPrintColumn+1, kmerDistance )


        sheet1Row = sheet1Row + 1
            # f = open('compareResult.txt', 'a+')
            # f.writelines("%s\n" % ("jaccard similarity between "+ f_item_i[0] +" and " + f_item_j[0] +"is : " + str(jaccard_similarity(f_item_i[1], f_item_j[1]))) )
            # f.close()
    # csv_file = open('p_data.csv',mode=)
    wb.save('Attributesv.xls')

    xls_file = pd.read_excel('Attributesv.xls', sheet_name="Attributes")
    xls_file.to_csv('Prediction_Data.csv', index=False)
    print ("time for comparing = ", time.time()-comparingStartTime)

    print("~~~~~~~~~~~~~~~~~~~finished~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



if __name__ == '__main__':
    main()

