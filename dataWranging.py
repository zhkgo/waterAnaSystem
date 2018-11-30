#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from getData import *
from nameList import *
import re
from snownlp import SnowNLP
import jieba
#sql data to pandas DataFrame
stopwords=['',' ','的','工作','建设','\n','了','工程','水利','水利局' ,'水利工程','工程','本站','发布','时间','负责人','一步','标准','重视']

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
def myCal(content,keys):
    #count the appear times of key in content 
    part_count={}
    for item in keys:
        part_count[item]=len(re.findall(item,content))
    part_pairs=zip(part_count.values(),part_count.keys())
    part_pairs=sorted(part_pairs)
    labels=[x[1] for x in part_pairs]
    values=[x[0] for x in part_pairs]
    return labels,values

def sumValues(content,mp):
    cities=list(set(mp.values()))
    labels,values=myCal(content,cities)
    result={}
    for label,value in zip(labels,values):
        result[label]=value
    labels,values=myCal(content,list(mp.keys()))
    for label,value in zip(labels,values):
        result[mp.get(label,'_')]=result.get(mp.get(label,'_'),0)+value
    return result


def getCntYears():
    df=getTitleDF()
    cntYears={}
    for i in range(len(df)):
        cntYears[df['time'][i].year]=cntYears.get(df['time'][i].year,0)+1
    return cntYears
def getDataByDate():
    columns=['title','content','time','origin']
    data=loadTotTable()
    data_init=toDataFrame(data,columns)
    data_init['time']=pd.to_datetime(data_init['time'])
    dataByDate=data_init.set_index('time')
    return dataByDate

def getQuaterlyData(bl=True):
    quaterly=[]
    contentsByQ=[]
    dataByDate=getDataByDate()
    for i in range(2013,2019):
        for j in range(4):
            quaterly.append(str(i)+'Q'+str(j+1))
            ttemp=""
            for k in range(j*3+1,j*3+4):
                temp=dataByDate[str(i)+'-'+str(k)]
                ttemp+=" ".join(temp['title'])
                if(bl):
                    ttemp+=" ".join(temp['content'])
                if(bl):
                    ttemp+=" ".join(temp['origin'])
            contentsByQ.append(ttemp)
    return quaterly,contentsByQ

def getRankData():
    snsData=pd.DataFrame()
    quaterly,contentsByQ=getQuaterlyData()
    mp=getMapOfCity()
    for q,content in zip(quaterly,contentsByQ):
        ret=sumValues(content,mp)
        for key,value in zip(ret.keys(),ret.values()):
            snsData=snsData.append(pd.Series({'q':q,'city':key,'value':value}),ignore_index=True)
    snsData.city.name='城市'
    snsData.q.name='季度'
    snsData.value.name='新闻数'
    snsData=snsData.sort_values(by='value',axis=0,ascending=False)
    snsData['rankt']=list(range(1,len(snsData)+1))
    snsData.rankt.name='热点指数排名'
    snsData.city.name='城市'
    snsData.q.name='季度'
    snsData.value.name='热点指数'
    snsData.rankt.name='热点指数排名'
    return snsData
def getEmotion(content):
    s = SnowNLP(content)
    i=0
    tot=len(s.sentences)
    print(tot)
    ls=[]
    for sentence in s.sentences:
        ls.append(SnowNLP(sentence).sentiments)
    return ls
def getEmotionTot(contents):
    result=[]
    i=0
    tot=len(contents)
    for content in contents:
        result.append(getEmotion(content))
        print(str(i/tot*100)+'%')
        i+=1
    return result
def trans(ls):
    #trans ls to point if emotion>0.95 then add one
    i=0
    for item in ls:
        if item>0.95:
            i+=1
    return i/len(ls)*100

def getEmotionDictM():
    quaterly,titlesByQ=getQuaterlyData(False)
    #print(len(quaterly),len(titlesByQ))
    result=getEmotionTot(titlesByQ)
    k=[trans(item) for item in result]
    dictM=pd.DataFrame({'季度':quaterly,'情感指数':k})
    dictM=dictM.set_index('季度')
    return dictM

def is_ok(s):
    return s not in stopwords
def get_most(content):
    wordlist=jieba.cut(content,cut_all=True)
    wordlist=list(filter(is_ok, wordlist))
    return pd.Series(wordlist).value_counts()
def standard(pairs):
    pairs=list(pairs)
    tot=sum(pairs[1])
    pairs[1]=[item/tot*100 for item in pairs[1]]
    return pairs
def getKeysData(keys):
    contentsByQ=getQuaterlyData()[1]
    ans=[standard(myCal(item,keys)) for item in contentsByQ]
    columns=ans[0][0]
    Dict={key:[] for key in columns}
    for item in ans:
        for key,value in zip(item[0],item[1]):
            Dict[key].append(value)
    dates=pd.date_range('2013-1-1','2018-11-1',freq='3M')
    df=pd.DataFrame(Dict)
    df.index=dates
    return df

def getHotWordsData():
    return getKeysData(getHotWords())

def getHotHumanData():
    return getKeysData(getHuman())
def getHotHumanData1():
    return getKeysData(getHuman1())
