#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from getData import *
from nameList import *
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