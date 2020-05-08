#Update the phylogenetic tree

* **This section explains how to update the phylogenetic tree by adding a new specie.**
* **For a instance, lets add new specie F to existing tree with species A,B,C,D and E**
* **First populate the sample_sequences folder with all the sequences(including the new sequence)**
*       So sample sequences folder will contain fasta sequences of A,B,C,D,E and F
* **Construct the k-mer forests for all sequences and populate sample_kmer_forests folder**
*       So sample_kmer_forests folder will contain kmer_forests for A,B,C,D,E and F
* **Go to the feature_extraction_a.py script and update 
'kmer_forests_path' to the sample_kmer_forests folder path, 'extracted_features_path' to the extracted_features folder path.
Execute the script and extracted_features folder will be populated with levelwise features**
* **Go to the feature_extraction_b.py script and update 'filePath' with sample_sequences folders path.
Execute the script and ACTGcount.txt will be created which contain total ACTG features.**
* **Go to the feature_extraction_c.py script and set following path values**
*       filePath = sample_sequences folders path
*       kmerACTGFilePath = extracted_features folder path
*       ACTGcountFile = path of the ACTGcount.txt
*       new_specie_file = Name of the fasta file of the new specie. Ex: F.fna
* **Execute the script and Prediction_Data.csv will be created.**


* **Neural model is already trained for more than 30,000 sequences and has about 85% accuracy. No need to traing again.(If requred to modify see NN_predecting_nearest_neighbour.py)
Trained model file and its weights are avialable as model.json and model.h5**
* **Go to Update_tree.py script and set following path values.**
*       json_file = path of the model.json
*       loaded_model.load_weights("XXXX") - XXXX should be the path for the weights file(model.h5)
*       predict_data = pd.read_csv('XXXX') - XXXX should be the path of Prediction_Data.csv
* **Execution of this script will tell the nearest neighbour of F out of A,B,C,D and E. Then it will append as a sibling of nearest neighbour. Updated tree will be shown.**
* **Following is an example updation, adding Acetobacter_Pasteurianus to existing tree**
![Phylogenetic-Tree-Construction](https://raw.githubusercontent.com/gihanmora/Phylogenetic_tree_construction/master/Diagram/updation.PNG)

