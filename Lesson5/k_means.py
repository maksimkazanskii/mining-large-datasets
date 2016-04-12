import numpy as np

N=10 #Number of centroids
def distance(a,b):
    return (a[0]-b[0])+(a[1]-b[1])

def change_posession(data,centroids):
    for item in data:
        closeness=10**10
        for centroid in centroids:
            if distance(centroid,item)<closeness:
                item[2]=centroid[2]
                closeness=distance(centroid,item)
    return data



def recalculate_centroids(data,centroids):
    for centroid in centroids:
        centroid[1]=0.0
        centroid[0]=0.0
        
    # Not too very efficient part
    #( first, we should iterate with "item" than with "centroid" instead)
    
    for centroid in centroids:
        count=0.0
        for item in data:
            
            if (item[2]==centroid[2]):
                count=count+1.0
                centroid[0]=centroid[0]+item[0]
                centroid[1]=centroid[1]+item[1]

        if (count>0):
            centroid[0]=centroid[0]/count
            centroid[1]=centroid[1]/count

    return centroids
    

data=np.array([[1.0,1.0][2.0,1.0],[2.0,2.0],[3.0,3.0],[4.0,2.0],[2.0,4.0],[4.0,4.0]])

centroids=np.array([
               [1.0,1.0,0],
               [4.0,4.0,1],
               ])

data=change_posession(data,centroids)
print(data)
centroids=recalculate_centroids(data,centroids)
print(centroids)
