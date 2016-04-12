#
# Simple PageRank algorithm
#


eps=1e-7
N=4
beta=1.0

import numpy as np


#
# Scheme should be adjusted according to N
#


rank=np.ones(N)

scheme= np.array([[0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0],
                  [0.25,0.25,0.25,0.25]])

d=np.zeros(N)
for i in range(0,N):
    for j in range(0,N):
        if (scheme[i][j]>0):
            d[i]=d[i]+1
print("Distribution of branches", d)

#
#
#

k=0.0
rank=np.ones(N)/N
rank_old=np.zeros(N)

while (k<=100):    
    rank_old=np.copy(rank)
    S=0.0
    rank_temp=np.zeros(N)
    for j in range(0,N):
        non_zero=np.flatnonzero(scheme[:,j])
        if (len(non_zero)==0):
            rank_temp[j]=0.0
        else:
            for i in range(0,len(non_zero)):
                 rank_temp[j]=rank_temp[j]+beta*rank[non_zero[i]]/d[non_zero[i]]
            
    rank=np.copy(rank_temp)
    print(k, rank)
    k=k+1 


