import numpy as np
import math
import  hashlib
#int(hashlib.sha1(s).hexdigest(), 16) % (10 ** 8)

N_hash=10**9

#
# Check the first pair
#

def my_hash_first(word1,word2,row_id):
    temp=word1+word2
    key=(int(hashlib.md5(temp).hexdigest(), 16) % (N_hash))
    if key in hash_dict_first:
        hash_dict_first[key].append((int)(row_id))
    else:
        hash_dict_first[key]=[(int)(row_id)]   
    return True

#
# Check the last pair
#

def my_hash_last(word1,word2,row_id):
    temp=word1+word2
    key=(int(hashlib.md5(temp).hexdigest(), 16) % (N_hash))
    if key in hash_dict_last:
        hash_dict_last[key].append((int)(row_id))
    else:
        hash_dict_last[key]=[(int)(row_id)]    
    return True

#
# Check weather the Livenstein distance is one or zero (Return True) or Return False
#


def levenshtein_simple(row1, row2):
   
   if math.fabs(len(row1)-len(row2))>=2:
       return False
   if math.fabs(len(row1)-len(row2))==0:
       mistake=0.0
       for i in range(0,len(row1)):
           if row1[i]!=row2[i]:
               mistake=mistake+1.0
           if mistake>=2.0:
               return False
       return True
   if math.fabs(len(row1)-len(row2))==1:
       if len(row1)>len(row2):
           large=row1
           small=row2
       else:
           large=row2
           small=row1

       for i in range(0,len(small)):
           if (large[i]!=small[i]):
              large.pop(i)
              if (large==small):
                  return True
              else:
                  return False
   return True

   

def equal(row1,row2)
   if row1==row2:
        return True
   else:
        return False
   
   
def check_candidates(listy):
    for i in range(0,len(listy)):
        for j in range(i+1,len(listy)):
            if (levenshtein_simple(data[(int)(listy[i])],data[(int)(listy[j])])):
                if not  equal(data[(int)(listy[i])],data[(int)(listy[j])]):
                    print(data[(int)(listy[i])],data[(int)(listy[j])]
            if (levenshtein_simple(data[(int)(listy[i])],data[(int)(listy[j])])):
                if (listy[i]>listy[j]):
                    pairs.add((listy[i],listy[j]))
                else:
                    pairs.add((listy[j],listy[i]))

i=0
data=[]
hash_dict_first={}
hash_dict_last={}
pairs=set()

#
#  Initialize hash function:
#


with open('sentences.txt') as f:
    for line in f:
        row=line.split()        
        my_hash_first(row[1],row[2],row[0])
        my_hash_last(row[len(row)-1],row[len(row)-2],row[0])
        row.pop(0)
        data.append(row)
        if (math.fmod(i,10000)==0):
            print(i)
        if (i>100000):
            break
        
        i=i+1
count=0
print("**************")
first_len=len(hash_dict_first)
last_len=len(hash_dict_last)
print(first_len," candidates from first pair")
print(last_len," candidates from second pair")
print("**************")    
    
for key in hash_dict_first:
    count=count+1
    if math.fmod(count,10000)==0:
        print(count," of ",first_len)
    check_candidates(hash_dict_first[key])
count=0

for key in hash_dict_last:
    count=count+1
    if math.fmod(count,10000)==0:
        print(count," of ",last_len)
    check_candidates(hash_dict_last[key])
print(len(pairs))


