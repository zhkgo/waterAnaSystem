#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataWranging import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

mpl.rcParams['figure.dpi']= 512
sns.set(style="dark",color_codes=True)
plt.style.use('seaborn-whitegrid')
plt.rc('axes', unicode_minus=False)  
mpl.rcParams['font.sans-serif'] = 'FZSongKeBenXiuKaiT-R-GB'
stopwords=['水利','水利局' ,'水利工程','工程','建设','本站','发布','时间','负责人','一步','标准','重视','责编','同时','街道','目前','会上','下一步','近日','近年来','据悉','据了解','此外','日前','他强调','按照','其中']
fontPath="fonts/fangzheng.ttf"

def showCloud(words,title):
    mycloud=WordCloud(font_path=fontPath,width=6400,height=3200,stopwords=stopwords).generate(words)
    plt.imshow(mycloud)
    plt.axis("off")
    mycloud.to_file(title)
    plt.show()
    return mycloud

def showTitleWordCloud():
    df=getTitleDF()
    text=" ".join(list(df['title']))
    wordlist=jieba.cut(text,cut_all=True)
    wl_space_split=" ".join(wordlist)
    showCloud(wl_space_split,"titleCloud.png")

def showContentWordCloud():
    contents=getAllContents()
    showCloud(contents,"contentsCloud.png")
def showBar(labels,values,top=10):
    plt.bar(range(top),values[-top:],fc='b',tick_label=labels[-top:])

def showCountry():
    content=getAllContents()
    religions=getReligions()
    keys=list(religions['下辖'])
    labels,value=myCal(content,keys)
    showBar(labels,value)
    plt.xlabel(u'县级市')
    plt.ylabel(u'提及次数')
    plt.title(u'提及次数排名前十')
    plt.show()

def showCitys():
    content=getAllContents()
    religions=getReligions()
    keys=list(set(religions['行政']))
    labels,value=myCal(content,keys)
    showBar(labels,value)
    plt.xlabel(u'地级市')
    plt.ylabel(u'提及次数')
    plt.title(u'提及次数排名前十')
    plt.show()

def showPie(keys):
    content=getAllContents()
    labels,values=myCal(content,keys)
    valuesum=sum(values)
    expl=[0.1 if x/valuesum >0.2 else 0 for x in values]
    plt.axis('equal')
    plt.pie(values,labels=labels,pctdistance=0.6,autopct='%1.2f%%',explode=expl,textprops = {'fontsize':6, 'color':'black'},shadow=True)
    
def showHotPie():
    keys=getHotWords()
    showPie(keys)
    plt.title('水利热词')
    
def showNewsYear(l,r):
    r+=1
    cntYears=getCntYears()
    names=[str(x) for x in range(l,r)]
    x=range(len(names))
    y=[cntYears[i] for i in range(l,r)]
    plt.plot(x,y,marker='*',mec='r',mfc='w',label='水利厅历年发文数量曲线图')
    plt.legend()
    plt.xticks(x,names,rotation=45)
    plt.show()

def showHotRankOfCity():
    snsData=getRankData()
    sns.boxplot(snsData.city,snsData.rankt)
    plt.title('浙江各大城市热点指数排名')
    plt.show()
def showNumbersOfCity():
    snsData=getRankData()
    sns.boxplot(snsData.city,snsData.value)
    plt.title('浙江各大城市热点指数')
    plt.show()

def showEmotionByQ():
    dictM=getEmotionDictM()
    dictM.plot(kind='barh',rot=0,color='r',title='各个季度情感指数')

def showHotWords():
    hotWords=getHotWordsData()
    hotWords.plot(title='历年水利热词')
    plt.xlabel('年份')
    plt.ylabel('热力值')
    plt.show()
def showHotHuman():
    hotHuman=getHotHumanData()
    hotHuman.plot(title='历年水利人物图壹')
    plt.xlabel('年份')
    plt.ylabel('热力值')
    #plt.savefig('human.jpg')
    plt.show()
def showHotHuman1():
    hotHuman=getHotHumanData1()
    hotHuman.plot(title='历年水利人物图贰')
    plt.xlabel('年份')
    plt.ylabel('热力值')
    #plt.savefig('human.jpg')
    plt.show()
def showHotValue(city,dateStart,dateEnd):
    keys=getHotWords()[:7]
    data=getKeysInCity(keys,city,dateStart,dateEnd)
    #print(data.head())
    data.plot(title=city+'各时间段热点词指数')
    plt.xlabel('时间')
    plt.ylabel('热力值')
def test():
    showHotValue('绍兴','2017','2018')
