specieName = []
distance_matrix = []

# Search according to name of species
# Param specie_name=specie_name , lines=read_kmer_results_file
def searchDistance(specie_name,specie_name_2,lines):
    specie_distance = []
    for line in lines:
        if ((line.split(",")[0]== specie_name and line.split(",")[1] == specie_name_2)
            or line.split(",")[0] == specie_name_2 and line.split(",")[1] == specie_name
        ):
            return (float(line.split(",")[2].rstrip()))
    return specie_distance

def distanceMatrixGenerator(file_path):
    with open(file_path) as f:
        lines = f.readlines()

        for i in range(0,len(lines)):
            specie_n = lines[i].split(",")[0]
            if specie_n not in specieName:
                specieName.append(specie_n)

        # print(specieName)

        distance_matrix = []
        for i in range(0,len(specieName)):
            dis = []
            # Construct empty specie list
            for j in range(0,i):
                dis.append("**")

            for j in range(i,len(specieName)):
                dis.append(searchDistance(specieName[i],specieName[j],lines))
            distance_matrix.append(dis)


        # print(distance_matrix)

        # Transpose
        for i in range(0,len(specieName)):
            for j in range(0,len(specieName)):
                distance_matrix[j][i] = distance_matrix[i][j]

    f.close()

    return specieName,distance_matrix