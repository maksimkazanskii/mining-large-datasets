#
# Simple PageRank algorithm
#


eps=1e-7
N=3
beta=0.85

import numpy as np


#
# Scheme should be adjusted according to N
#


rank=np.ones(N)

scheme= np.array([[0.0, 1.0/2.0, 1.0/2.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]])

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

while (np.linalg.norm(rank-rank_old)>eps*N):    
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
            
    for j in range(0,N):
         S=S+rank_temp[j]
    for j in range(0,N):
        rank[j]=rank_temp[j]+(1.0-S)/N
    k=k+1 
    print(rank)
rank=3*rank
a=rank[0]
b=rank[1]
c=rank[2]

print("1", a - c - 0.15*b)
print("2", 85*b-0.575*a+0.15*c)
print("3", 0.95*a-0.9*c-0.05*b )
print("4", c - b -0.575*a )


