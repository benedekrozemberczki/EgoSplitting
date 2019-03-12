Ego-splitting Framework
============================================
A NetworkX implementation of "Ego-splitting Framework: from Non-Overlapping to Overlapping Clusters" (KDD 2017)
<p align="center">
  <img width="800" src="egonet.jpg">
</p>
<p align="justify">
We propose a new framework called Ego-Splitting for detecting clusters in complex networks which leverage the local structures known as ego-nets (i.e. the subgraph induced by the neighborhood of each node) to de-couple overlapping clusters. Ego-Splitting is a highly scalable and flexible framework, with provable theoretical guarantees, that reduces the complex overlapping clustering problem to a simpler and more amenable non-overlapping (partitioning) problem. We can solve community detection in graphs with tens of billions of edges and outperform previous solutions based on ego-nets analysis.

More precisely, our framework works in two steps: a local ego-net analysis phase, and a global graph partitioning phase . In the local step, we first partition the nodes’ ego-nets using a partitioning algorithm. We then use the computed clusters to split each node into its persona nodes that represent the instantiations of the node in its communities. Then, in the global step, we partition the newly created graph to obtain an overlapping clustering of the original graph.</p>

This repository provides a lightweight NetworkX implementation of Ego-splitting as described in the paper:

> Ego-splitting Framework: from Non-Overlapping to Overlapping Clusters.
> Alessandro Epasto, Silvio Lattanzi, and Renato Paes Leme.
> KDD, 2017.
> [[Paper]](https://www.eecs.yorku.ca/course_archive/2017-18/F/6412/reading/kdd17p145.pdf)

### Requirements
The codebase is implemented in Python 3.5.2. package versions used for development are just below.
```
networkx          1.11
tqdm              4.28.1
pandas            0.23.4
texttable         1.5.0
argparse          1.1.0
```
### Datasets

The code takes the **edge list** of the graph in a csv file. Every row indicates an edge between two nodes separated by a comma. The first row is a header. Nodes should be indexed starting with 0. A sample graph for `Cora` is included in the  `input/` directory. In addition to the edgelist there is a JSON file with the sparse features and a csv with the target variable.

### Options
Training an NGCN model is handled by the `src/main.py` script which provides the following command line arguments.

#### Input and output options
```
  --edge-path       STR    Edge list csv.         Default is `input/cora_edges.csv`.
  --features-path   STR    Features json.         Default is `input/cora_features.json`.
  --training-size     INT     Training set size.             Default is 1500.
  --validation-size   INT     Validation set size.           Default is 500.
  --learning-rate     FLOAT   Adam learning rate.            Default is 0.01
  --dropout           FLOAT   Dropout rate value.            Default is 0.5
  --layers            LST     Layer sizes for model.         Default is [64, 64, 64]. 
```
### Examples
The following commands learn a neural network and score on the test set. Training a model on the default dataset.
```
python src/main.py
```
<p align="center">
<img style="float: center;" src="ngcn_run.jpg">
</p>

Training an NGCN model for a 100 epochs.
```
python src/main.py --epochs 100
```
Increasing the learning rate and the dropout.
```
python src/main.py --learning-rate 0.1 --dropout 0.9
```
Training a two layer model:
```
python src/main.py --layers 64 64
```

