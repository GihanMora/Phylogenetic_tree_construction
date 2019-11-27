#Genetic Distance Calculation Using Kmer forests
##Kmer listing
1.	Populate DNA_Sequences folder with required FASTA sequences.
2.	Configure DSK Tool. https://github.com/GATB/dsk
3.	Go to kmer_listing folder and copy statup.properties file, kmer_listing.sh files to the bin folder of DSK tool.
4.	Change the GENOME_DIRECTORY and OUTPUT_DERECTORY paths in startup.properties to DNA_Sequences folder path and DSK_results folder path.
5.	Run kmer_listing.sh file using “sh kmer_listing.sh”
6.	Now you get outputs of DKS tool in DSK_results folder.
##Kmer forest comparison
1.	Change CVS_operations.py file CSV_Path to CSV_results folder path and DKS_Path to DSK_results folder path and run the script. Converted CSV files will be in CSV_results folder.
2.	Open up Kmer_distance_calculation.py and change the csv_file_list_path to path of CSV_results folder path.
3.	Run kmer_distance_calculation.py and a text file will be created with results.
