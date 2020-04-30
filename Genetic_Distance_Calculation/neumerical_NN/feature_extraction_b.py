import os
import xlwt
from xlwt import Workbook

filePath = "sample_sequences/"
# wb = Workbook()
# sheet1 = wb.add_sheet('ACTG differences')
# sheet2 = wb.add_sheet('ACTG counts')

fileNameArray = []
for filename in os.listdir(filePath):
    fileNameArray.append(filename)
print(fileNameArray)

counts = []
sheet2Row = 0
for fileName in fileNameArray:

    file1 = open(filePath + fileName, "r")
    dnaSet = file1.read()

    countA = 0;
    countC = 0;
    countT = 0;
    countG = 0;


    for i in dnaSet:
        if(i=='A'):
            countA = countA+1

        if (i == 'C'):
            countC = countC+1

        if (i == 'T'):
            countT = countT+1

        if (i == 'G'):
            countG = countG+1

    # sheet2.write(sheet2Row, 0, fileName)
    # sheet2.write(sheet2Row, 1, countA)
    # sheet2.write(sheet2Row, 2, countC)
    # sheet2.write(sheet2Row, 3, countT)
    # sheet2.write(sheet2Row, 4, countG)
    counts.append([fileName,[countA, countC, countT, countG]]);
    # sheet2Row = sheet2Row + 1

countText = open('ACTGcount.txt', 'w')
countText.write(str(counts))
countText.close();

print (counts)
excelRow = 0;
# for i in range(0, len(counts)-1):
#     for j in range (i+1, len(counts)):
#         diffA = counts[i][1][0] - counts[j][1][0]
#         diffC = counts[i][1][1] - counts[j][1][1]
#         diffT = counts[i][1][2] - counts[j][1][2]
#         diffG = counts[i][1][3] - counts[j][1][3]
#
#         sheet1.write(excelRow, 0, counts[i][0])
#         sheet1.write(excelRow, 1, counts[j][0])
#         sheet1.write(excelRow, 2, abs(diffA))
#         sheet1.write(excelRow, 3, abs(diffC))
#         sheet1.write(excelRow, 4, abs(diffT))
#         sheet1.write(excelRow, 5, abs(diffG))
#
#         excelRow = excelRow + 1


# wb.save('ACTG_differences.xls')



