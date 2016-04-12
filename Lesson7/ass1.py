#
# Topic specific PageRank with teleport nodes 1 and 2
#( the weight assigned for node 1 is twice that of node 2)
#
# The general alglorithm could be assigned to any graph.
# Yet is not parrallel.
#
#

epsilon=10-5

import numpy as np

#
# Normalizing 1D list
#

def normalize(listy):

    summy=0.0

    for item in listy:
        summy=summy+item

    if (summy>0):
        for i in range(0,len(listy)):
            listy[i]=listy[i]/summy
            print(item)
            
    return listy


#
# Scheme should be adjusted according to N
#



N=4
beta=0.7
rank=np.ones(N)

#
# !!! from the i (row) to j(column) connection 
#
scheme= np.array([[0.0, 0.5, 0.5, 0.0],
                  [1.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0],
                  [0.0, 0.0, 1.0, 0.0]])

#
# Teleport rates. 
#

teleport_weight=np.array([2.0,1.0,0.0,0.0])
teleport_weight=normalize(teleport_weight)
teleport_indexes=np.flatnonzero(teleport_weight)
N_teleport=len(teleport_indexes)

print(teleport_weight,teleport_indexes,N_teleport)

#
# d - number of output branches from i-node
#

d=np.zeros(N)

for i in range(0,N):
    for j in range(0,N):
        if (scheme[i][j]>0):
            d[i]=d[i]+1
print("Distribution of branches", d)


#
#   k - number of steps. Here the number_of_step scheme was implemented.
#   (Not a convergence scheme).
#

k=0.0
rank=np.ones(N)/N

while (k<=50.0):
    S=0.0
    rank_temp=np.zeros(N)
    for j in range(0,N):

        #
        # Non_Zero - List of indexes that are non-zero.
        #
        
        non_zero=np.flatnonzero(scheme[:,j])
        if  (len(non_zero)==0):
            rank_temp[j]=0.0
        else:
            for i in range(0,len(non_zero)):
                 rank_temp[j]=rank_temp[j]+beta*rank[non_zero[i]]/d[non_zero[i]]

    #
    # Aggregate leaked PageRank
    #
    
    for j in range(0,N):
         S=S+rank_temp[j]
    
    #
    # Distribution over the teleports
    #
    
    for j in range(0,N):
        if (j in teleport_indexes):
            rank[j]=rank_temp[j]+teleport_weight[j]*(1.0-S)
        else:
            rank[j]=rank_temp[j]
        
    k=k+1
    print(rank)


