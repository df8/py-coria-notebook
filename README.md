# CORIA Python Library + Jupyter Notebook (py-coria-notebook)

CORIA (Connectivity Risk Analyzer) is a framework for analyzing network connectivity weaknesses on graphs with millions of vertices and edges.

This repository contains development of a wrapper library around the frameworks Pandas, NetworkX, cuDF and cuGraph with the purpose to analyse network connectivity risks.

This master's thesis 

## Supported Algorithms
1. All-Pairs Shortest Paths (APSP)
2. Node Degree (NDEG)
3. Average Neighbour Degree (AND)
4. Iterated Average Neighbour Degree (IAND)
5. Local Clustering Coefficient (CLCO)
6. Betweenness Centrality (BC)
7. Average Shortest Path Length (ASPL)
8. Eccentricity (ECC)
9. Unified Risk Score (URS)
10. Connectivity Risk Classification (CRC)
11. Min-Max Normalisation


## How to run the Jupyter Notebook on a local workstation (Linux only)
1. Install Anaconda
2. Visit https://rapids.ai/start.html#get-rapids and select your system configuration to generate a command starting with `conda create ...`. We tested on Ubuntu 18.04 with CUDA 11.0.
1. Clone this repository to your PC.
2. Browse with your Jupyter Notebook file manager to the direction of CORIA-Notebook-v1.0.ipynb and open this file
3. Run the cells.


## How to run the Jupyter Notebook in BlazingSQL
1. Visit app.blazingsql.com, Login
2. Create a new project based on this Github repository
3. Use the file browser in the BlazingSQL to open the file CORIA-Notebook-v1.0.ipynb from this repo. 



## My supplementary publication
- Fradin, David Alexander (2020). Accelerating the Analysis of Network Connectivity Risks: Development of High-Performance Software Modules on the GPU [Master’s thesis]. Humboldt-Universität zu Berlin.