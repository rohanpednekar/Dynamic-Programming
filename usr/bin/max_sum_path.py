#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  max_sum_path.py
#  
#  Copyright 2014 Rohan Pednekar <rohanpednekar08@gmail.com>
#  
import time
# a list to represent the tree
tree = []
# read the data file
data_file = open("tree.dat", "r")
# for each line in the data file, append list to the tree
for line in data_file:
    row = [int(i) for i in line.split(" ")] 
    tree.append(row)
start_time = time.time()
# for each node in the tree, add the max of the cells below-left and
# below-right. the node at the top will contain the greatest sum from bottom to top
for i in range(len(tree)-2,-1,-1):
    for j in range(i+1):
        tree[i][j] +=  max([tree[i+1][j],tree[i+1][j+1]])
end_time = time.time() - start_time
print "Maximum sum of path numbers: %d" % (tree[0][0])
print "Total execution time: %f seconds" % (end_time)
