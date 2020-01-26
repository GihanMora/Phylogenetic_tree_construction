# Phylogenetic Tree Construction and Updation Workflow

From this research we propose two novel alignment-free, pairwise, distance calculation methods based on k-mers and locality sensitive hashing. In addition to that, we proposed a machine learning-based phylogenetic tree construction mechanism. With the proposed approaches we can gear up the efficiency and accuracy of genetic distance calculation.
The tree construction method which is based on a modified version of k medoid is also guaranteed to provide significant performance compared to traditional phylogenetic tree construction methods. As the final part of the research, we implemented a numerical neural network to efficiently update the phylogenetic tree. So in summary with this research, we implemented novel methods of genetic distance calculation, phylogenetic tree construction, and tree updation.


## Introduction

The phylogenetic tree (Evolutionary tree) is a branching diagram that shows the evolutionary relationships among various organisms. It branches out species by considering the similarities of them based on the genetic distance. Phylogenetic tree can be considered as one of the fundamental components of most of the bioinformatic research.

![Phylogenetic-Tree-Construction](https://raw.githubusercontent.com/ngimhana/Phylogenetic_tree_construction/master/Diagram/phylogenetic-tree.png)


## Research Problem

As explained above phylogenetic trees can be used as a concise and informative way of giving details about set of species. Phylogenetic tree plays a vital role in doing comparisons between species and it helps to get an idea about genetic and physical characteristics about a particular species. So that, for scientific experiments phylogenetic tree has become an essential prerequisite. In order to construct the phylogenetic tree first it is required to calculate genetic distances.
Genetic distance calculation methods can be classified into two main categories namely alignment based and alignment free distance calculation. But when we are considering about existing methods of genetic distance calculation there are several limitations. Generally alignment based methods of genetic distance calculation are heuristically bounded. For an example, alignment based algorithms such as BLAST use many heuristics in extending hits, scoring for hits, picking diagonal with max hits etc. Because of such heuristics the accuracy is reduced as results are bounded on those heuristics. Addition to that alignment based methods assumes that homologous sequences comprise a series of linearly arranged sequence stretches. However, in real-world this assumption is very often violated.

In alignment free methods most of the time raw genetic sequence is estimated by some procedure. After that in order to calculate the genetic distance they are using these estimations rather than raw genetic sequences. So in these methods also accuracy is reduced by a considerable amount. 
Addition to that when considering existing tree construction methods again there are several limitations. Most of the current phylogenetic tree construction methods are based on UPGMA method. In this method there are considerable amount of repeated work as in each iteration we need to reconstruct the distance matrix. So efficiency is drastically reduced in those UPGMA based methods. Additionally these methods are using a bottom up approach to construct the tree which again cause to reduce the accuracy as does not consider all the distances once.

Another major requirement of phylogenetic tree is it is required to be updated according to the new species discoveries. But with the enhancement of science, day by day new species are identified as a result of thousands of experiments being done in laboratories. According to the National Geographic 86% of species of the earth are still unknown and various researches are ongoing in different aspects of discovering those. 
 
As scientists are discovering a new set of species each year, phylogenetic trees are also required to be updated according to the latest findings in order to give correct information. With the above mentioned approaches, if a new genome sequence (aka new species) is added to that initial genome sequence set, it has to go back to the beginning and construct the phylogenetic tree again from zero. So, with these existing approaches updating a tree is really inefficient and consumes a considerable amount of time and resources. So, when considering the rate of discovering new species and generating phylogenetic trees relevant to them has become an exhausting duty today. These facts reflect the requirement of an efficient way of generating phylogenetic trees in a dynamic manner without changing the entire tree.


## Methodology

![Phylogenetic-Tree-Construction-methodology](https://raw.githubusercontent.com/ngimhana/Phylogenetic_tree_construction/master/Diagram/methodology.png)

From this research, present a phylogenetic tree construction and updation workflow in order to address the shortcomings of existing methods. This workflow consists of 3 main stages as follows

1. **Distance Calculating Stage** : Consist of genetic distance calculation method based on kmer forest construction and comparison. As the 2nd part of the distance calculation, here I used a Locality Sensitive Hashing Method for constructing genetic distances for species in different kingdoms.
2. **Tree construction stage** : Here phylogenetic tree is constructed using K-Medoid algorithm.
3. **Tree updation stage** : Consist of numerical neural network to dynamically add new species to the constructed tree.

During the first stage the usage of a novel genetic distance calculation method to get the genetic distance between species. In order to do that, building a kmer forest using the distinct kmers extracted from the raw genetic sequences. Afterwards, usage of specified tree pruning algorithm to compare those forests to get the genetic distance. From the kmer forests, represention of raw genetic sequences in very compact and informative manner. Because of the compactness of kmer forests and the pruning mechanisms it allows to very efficiently calculate the genetic distance. Addition to that as it considers both common and distinct kmer into consideration when calculating genetic distance it gives very high sensitivity compared to existing genetic distance calculation methods. 

In the second stage of the workflow we are using the calculated genetic distances  to construct phylogenetic trees using unsupervised machine learning method K-medoid clustering. With this we can reduce the amount of repeated work from huge amount compared to the methods such as UPGMA. Additionally it rises the accuracy as it used top down approach where it consider whole image when subdividing species. So it can be stated that this method of tree construction has  high accuracy and efficiency compared to existing methods of tree construction.

The third stage of the workflow we are presenting a numerical neural network to efficiently update the phylogenetic tree by adding a new species to already constructed tree. This process does not require building the tree from the beginning in existing methods such as maximum parsimony. Here when new species encountered neural networks predict the nearest neighbor in the existing phylogenetic tree. Afterward new specie is added to the corresponding nearest neighbor.
