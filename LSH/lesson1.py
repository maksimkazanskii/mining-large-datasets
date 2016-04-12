import numpy as np
import math
import  hashlib
#int(hashlib.sha1(s).hexdigest(), 16) % (10 ** 8)

k=5
N_hash=10**9
def shingles(row):
    listy=[]
    for i in range(0,len(row)-k):
        temp=""
        for j in range(0,k):
            temp=temp+row[i+j]    
            listy.append(int(hashlib.md5(temp).hexdigest(), 16) % (N_hash))
    return listy


def add_cand(candidates,stack):
    if (len(stack)==0):
        pass
    else:
        for k in range(0,len(stack)):
            for l in range(0,len(stack)):
                if k<l:
                    candidates.append((item1,item2))
    return candidates
i=0
data=[]
lang=set()
with open('sentences.txt') as f:
    for line in f:
        row=line.split()
        for item in shingles(row):
            data.append((row[0],len(row),item))
            lang.add(item)
        if (math.fmod(i,1000)==0):
            print(i)
        if (i>10000):
            break;
        i=i+1
print("Lang: ",len(lang))
sorted(data, key=lambda student: student[2])
print("Data :",len(data))
print(data[55])
candidates=[]
i=0
j=0

#while i<=N_hash:
#     stack=[]
#     while (data[j+1][2]==data[j][2]):
#         stack.append(data[j])             
#         j=j+1
#     candidates=add_cand(candidates,stack)
#     print(i)
#     i=i+1
#print(len(candidates))         
