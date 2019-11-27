# Genetic Distance Calculation Using Kmer forests
## Kmer listing

1.	Populate __DNA_Sequences__ folder with required FASTA sequences.

2.	Configure DSK Tool. https://github.com/GATB/dsk

3.	Go to __kmer_listing__ folder and copy _statup.properties_ file,
 _kmer_listing.sh_ files to the bin folder of DSK tool.

4.	Change the __GENOME_DIRECTORY__ and __OUTPUT_DERECTORY__ paths 
in _startup.properties_ to __DNA_Sequences__ folder path and 
__DSK_results__ folder path.

5.	Run kmer_listing.sh file using
      ```
      sh kmer_listing.sh
      ```
      
6.	Now you get outputs of DKS tool in __DSK_results__ folder.

## Kmer forest comparison

1.	Change _CVS_operations.py_ file __CSV_Path__ to __CSV_results__ folder 
path and __DKS_Path__ to __DSK_results__ folder path and run the script. 
Converted CSV files will be in __CSV_results__ folder.

2.	Open up _Kmer_distance_calculation.py_ and change the __csv_file_list_path__ 
to path of __CSV_results__ folder path.

3.	Run _kmer_distance_calculation.py_ and a text file 
will be created with results.
