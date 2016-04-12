#
# Simple PageRank algorithm
#


epsilon=10-5

import numpy as np


#
# Scheme should be adjusted according to N
#

N=3
beta=0.7
rank=np.ones(N)

scheme= np.array([[0.0, 1.0/2.0, 1.0/2.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])

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

while (k<=10.0):
    S=0.0
    rank_temp=np.zeros(N)
    for j in range(0,N):
        non_zero=np.flatnonzero(scheme[:,j])
        if (len(non_zero)==0):
            rank_temp[j]=0.0
        else:
            for i in range(0,len(non_zero)):
                 rank_temp[j]=rank_temp[j]+beta*rank[non_zero[i]]/d[non_zero[i]]
            
    for j in range(0,N):
         S=S+rank_temp[j]
    for j in range(0,N):
        rank[j]=rank_temp[j]+(1.0-S)/N
    k=k+1
    print(rank)

rank=3*rank
print("a+b",rank[0]+rank[1])
print("a+c",rank[0]+rank[2])
print("b+c",rank[1]+rank[2])
