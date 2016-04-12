
import numpy as np
import hashlib

def distance(old,new):
    return (old[0]-new[0])**2+(old[1]-new[1])**2

def find_farest(new_data,data):
    candidate_distance={}
    candidate_index={}
    candidate_item={}
    result_point=[]
    index=-1.0
    for old_item in data:
        index=index+1
        delta=1000000.0
        for new_item in new_data: 
            if distance(new_item,old_item)<delta:
                delta=distance(new_item,old_item)
            else:
                pass
        candidate_distance[(str(old_item))]=delta
        candidate_index[(str(old_item))]=index
        candidate_item[(str(old_item))]=old_item
    maximum_distance=0.0
    for old_key in candidate_distance.keys():
        print(candidate_distance[old_key], candidate_item[old_key])
        if candidate_distance[old_key]>maximum_distance:
            maximum_distance=candidate_distance[old_key]
            result_point=candidate_item[old_key]
            index=candidate_index[old_key]
    print("Result:", result_point,index)
    return (result_point,index)

data=np.array([[0.0,0.0],[10.0,10.0],[1.0,6.0],[3.0,7.0],[4.0,3.0],[7.0,7.0],[8.0,2.0],[9.0,5.0]])
new_data=np.array([[0.0,0.0],[10.0,10.0]])
data=np.delete(data,0,0)
data=np.delete(data,0,0)

while len(data)>0:
    (item,index)=find_farest(new_data,data)
    new_data=np.concatenate((new_data, [item]))
    print(index)
    print(data)
    data=np.delete(data, index,0)
    print("NEW_DATA:",new_data)
    print("OLD_DATA:",data)
