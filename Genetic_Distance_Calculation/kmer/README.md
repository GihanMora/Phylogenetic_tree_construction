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

4. Created kmer forests can be found in the kmer_forests folder

## Feature Extraction for Neural Network


1.	Open up the feature_extraction.py script in neumerical_NN folder. Change the variables
kmer_forests_path to the path where kmer forests stored. Change the extracted_features_path to where you want to store extracted features. Run the script.
Level wise ACTG count will be extracted.

## Adding new specie to existing phylogenetic tree

1.	Get the feature vectors of existing species of
 phylogenetic tree + the new specie 
and create a csv file containing features similar 
to the _Training_Data.csv_ file. You might required
to make kmer_forest for new specie. To extract 
features can refer __Feature Extraction for Neural 
Network__ section.

2.	With this features make prediction set. 
Rows of this prediction set should contain features(aka difference vectors) of new specie against all existing species.

3.	Give that to NN and it will predict the distances between existing specie and other species in the tree. Pick the neighbour
 with max similarity and plug new specie to there.
 
 
* Cite the publication if you are using this to credit authors. 
* [1]G. Gamage, N. Gimhana, A. Wickramarachchi, V. Mallawaarachchi, and I. Perera, “Alignment-free Whole Genome Comparison Using k-mer Forests,” in 2019 19th International Conference on Advances in ICT for Emerging Regions (ICTer), 2019, doi: 10.1109/icter48817.2019.9023714.
 