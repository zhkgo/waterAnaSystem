#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from getData import *
from nameList import *
import re
#sql data to pandas DataFrame
def toDataFrame(data,columns):
    test=list(zip(*data))
    tempDict={}
    for key,i in zip(columns,range(len(columns))):
        tempDict[key]=test[i]
    return pd.DataFrame(tempDict)
def getTitleDF():
    data=loadTitles()
    #格式化后放入pandas的DataFrame中
    return toDataFrame(data,['title','time'])
def getAllContents():
    contents=loadContent()
    fcontents=[content[0] for content in contents]
    contentall=" ".join(fcontents)
    return contentall
def getPositionDF():
    cities=getPosition()
    columns=['province','city','qu','lon','lat']
    cities.columns=columns
    cities['qu']=[item[:-1] for item in cities['qu']]
    cities['city']=[item[:-1] for item in cities['city']]
    return cities
def getMapOfCity():
    cities=getPositionDF()
    mp={key:value for key,value in zip(cities['qu'],cities['city'])}
    return mp
def my_cal(content,keys):
    #count the appear times of key in content 
    part_count={}
    for item in keys:
        part_count[item]=len(re.findall(item,content))
    part_pairs=zip(part_count.values(),part_count.keys())
    part_pairs=sorted(part_pairs)
    labels=[x[1] for x in part_pairs]
    values=[x[0] for x in part_pairs]
    return labels,values
