#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataWranging import *
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
mpl.rcParams['figure.dpi']= 512
sns.set(style="dark",color_codes=True)
mpl.rcParams['font.sans-serif'] = 'FZSongKeBenXiuKaiT-R-GB'

stopwords=['水利','水利局' ,'水利工程','工程','建设','本站','发布','时间','负责人','一步','标准','重视']
fontPath="fonts/fangzheng.ttf"
def showCloud(words):
    mycloud=WordCloud(font_path=fontPath,width=800,height=400,stopwords=stopwords).generate(words)
    plt.imshow(mycloud)
    plt.axis("off")
    plt.show()
    return mycloud

def showTitleWordCloud():
    df=getTitleDF()
    text=" ".join(list(df['title']))
    wordlist=jieba.cut(text,cut_all=True)
    wl_space_split=" ".join(wordlist)
    showCloud(wl_space_split)

def showContentWordCloud():
    contents=getAllContents()
    showCloud(contents)
def showBar(labels,values,top=10):
    plt.bar(range(top),values[-top:],fc='b',tick_label=labels[-top:])

def showCountry():
    content=getAllContents()
    keys=
    labels,value=my_cal(content,keys)
    plt.xlabel(u'县级市')
    plt.ylabel(u'提及次数')
    plt.title(u'提及次数排名前十')
    plt.show()

def showPie(keys):
    content=getAllContents()
    labels,values=my_cal(content,keys)
    valuesum=sum(values)
    expl=[0.1 if x/valuesum >0.2 else 0 for x in values]
    plt.axis('equal')
    plt.pie(values,labels=labels,pctdistance=0.6,autopct='%1.2f%%',explode=expl,textprops = {'fontsize':6, 'color':'black'},shadow=True)
    
def showHotPie():
    keys=getHotWords()
    showPie(keys)
    plt.title('水利热词')
    
    
