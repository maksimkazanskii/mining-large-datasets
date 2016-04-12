import numpy as np
import pprint
import random

def calculate_the_top(data):
    maximum=0.0
    exception_list=[]
    for item in data:
        if (item['Yield1']>maximum)&(item['Budget']>=item['Bid']):          
            first=item
            maximum=item['Yield1']
    exception_list.append(first)
    maximum=0.0
    for item in data:
         if (item['Yield2']>maximum)&(item['Budget']>=item['Bid'])&(item not in exception_list):
              second=item
              maximum=item['Yield2']
    exception_list.append(second)
    maximum=0.0
    for item in data:
         if (item['Yield3']>maximum)&(item['Budget']>=item['Bid'])&(item not in exception_list):
              third=item
              maximum=item['Yield3']
    return (first,second,third)


def update(first,second,third,data):
    print(first,second,third)
    for i in range(0,len(data)):
        if (data[i]['Advertiser']==first['Advertiser']):
            data[i]=first
        if (data[i]['Advertiser']==second['Advertiser']):
            data[i]=second
        if (data[i]['Advertiser']==third['Advertiser']):
            data[i]=third
            
    return data
data=[]
data.append({'Advertiser':'A','Bid':0.001,'CTR1':0.015,'CTR2':0.010,'CTR3':0.005,'Budget':1,'Click_number':0.0})
data.append({'Advertiser':'B','Bid':0.0009,'CTR1':0.016,'CTR2':0.012,'CTR3':0.006,'Budget':2,'Click_number':0.0})
data.append({'Advertiser':'C','Bid':0.0008,'CTR1':0.017,'CTR2':0.014,'CTR3':0.007,'Budget':3,'Click_number':0.0})
data.append({'Advertiser':'D','Bid':0.0007,'CTR1':0.018,'CTR2':0.015,'CTR3':0.008,'Budget':4,'Click_number':0.0})
data.append({'Advertiser':'E','Bid':0.0006,'CTR1':0.019,'CTR2':0.016,'CTR3':0.010,'Budget':5,'Click_number':0.0})
for item in data:
    item['Yield1']=item['Bid']*item['CTR1']
    item['Yield2']=item['Bid']*item['CTR2']
    item['Yield3']=item['Bid']*item['CTR3']
    
total_click_number=0.0

while (total_click_number<=10100.0):

    (first,second,third)=calculate_the_top(data)
    print(first['Advertiser'],second['Advertiser'],third['Advertiser'])
    while (first['Budget']>item['Bid'])&(second['Budget']>item['Bid'])&(third['Budget']>item['Bid']):

        rand=random.randint(1, 10000)
        
        if (rand<=first['CTR1']*10000.0):
            total_click_number=total_click_number+1.0
            first['Click_number']=first['Click_number']+1
            first['Budget']=first['Budget']-first['Bid']
                
        if (rand<=second['CTR2']*10000.0):
            total_click_number=total_click_number+1.0
            second['Click_number']=second['Click_number']+1.0
            second['Budget']=second['Budget']-second['Bid']

        if (rand<=third['CTR3']*10000.0):
            total_click_number=total_click_number+1.0
            third['Click_number']=third['Click_number']+1.0
            third['Budget']=third['Budget']-third['Bid']
    update(first,second,third,data)        

for item in data:
    print(item['Advertiser'], item['Click_number']/total_click_number)
