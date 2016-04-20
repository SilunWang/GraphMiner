#!/usr/bin/env bash
python plotScatter.py ../data/1_degreedist.csv degree_dist.png
python plotCCDF.py ../data/2_pagerank.csv pagerank_ccdf.png
python plotScatter.py ../data/3_component_size_dist.csv comp_dist.png
python plotScatter.py ../data/4_kvalue_dist.csv kcore_dist.png
python plotPDF.py ../data/5_radius_dist.csv radius_dist.png
python plotVS.py ../data/2_pagerank.csv ../data/8_degree.csv degreeVSpagerank.png
python plotVS.py ../data/kcore.csv ../data/8_degree.csv degreeVSkcore.png
python plotScatter.py ../data/eigval.csv eig.png

