import csv
import os
import pandas as pd
DSK_Path= "/home/castle/Phylogenetic_tree_construction/Genetic_Distance_Calculation/kmer/DSK_Results/"
CSV_Path= "/home/castle/Phylogenetic_tree_construction/Genetic_Distance_Calculation/kmer/CSV_Results/"

outputFileList=os.listdir(DSK_Path)
outputCSVFileList=os.listdir(CSV_Path)


# Output to CSV Conversion
def text_to_csv():
    for outputFile in outputFileList:
        with open(DSK_Path + outputFile, 'r') as in_file:
            print(outputFile + " Started Conversion...")
            stripped = (line.strip() for line in in_file)
            lines = (line.split(" ") for line in stripped if line)
            with open(CSV_Path + outputFile + '.csv', 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(('Kmer', 'Count'))
                writer.writerows(lines)
        print(outputFile + " Ended Conversion...")


def convert_csv_column_to_list(filename):
    dataframe = pd.DataFrame(pd.read_csv(filename))
    return list(dataframe['Kmer'])

# Convert kmer results to CSV
text_to_csv()
