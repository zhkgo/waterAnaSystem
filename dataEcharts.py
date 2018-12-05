#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataWranging import *
from pyecharts import HeatMap, Map,Style,Pie,Kline
from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig
from pyecharts import Bar, Line, Grid
from pyecharts import Geo


def showCountry():
    content=getAllContents()
    religions=getReligions()
    keys=list(religions['下辖'])
    labels,values=myCal(content,keys)
    bar = Bar("提及次数前十")
    #其他主题：vintage,macarons,infographic,shine，roma 
    bar.use_theme("shine")
    bar.add("",labels[-10:],values[-10:],is_stack=True)
    bar.xaxis_name='县级市'
    bar.yaxis_name='提及次数'
    #bar.render()
    return bar
def showHotMap():
    df=getMerge()
    geo_cities_coords={df.iloc[i]['qu']:(df.iloc[i]['lon'],df.iloc[i]['lat'])
                    for i in range(len(df))}   
    attr=list(df['qu'])
    # [df.iloc[i][' ar']/500 for i in range(len(df))]
    value=list(df['values'])
    print(type(value[0]))
    print(type(attr[0]))
    style = Style(title_color= "#fff",title_pos = "center",width =800,height = 600,background_color = "#132F3D")
    geo = Geo('浙江水利厅发文热力图',**style.init_style)
    geo.add("",attr,value,visual_range=[0,8000],symbol_size=15,
        visual_text_color= "#fff",is_piecewise = True,
        is_visualmap= True,maptype = '浙江',
        geo_cities_coords=geo_cities_coords)
    #geo.render('浙江水利厅发文热力图.html')
    return geo

def showCitys():
    content=getAllContents()
    religions=getReligions()
    keys=list(set(religions['行政']))
    labels,values=myCal(content,keys)
    bar = Bar("提及次数前十")
    #其他主题：vintage,macarons,infographic,shine，roma 
    bar.use_theme("infographic")
    bar.add("",labels[-10:],values[-10:],is_stack=True)
    bar.xaxis_name='地级市'
    bar.yaxis_name='提及次数'
    bar.render()
    return bar

def showHotPie():
    keys=getHotWords()
    content=getAllContents()
    labels,values=myCal(content,keys)
    pie = Pie("水利热点比例图", title_pos='center')
    #pie.add("",labels,values,is_label_show=True)
    pie.add(
    "",
    labels,
    values,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
	)
    pie.render()
    return pie
def showNewsYear():
    l=2010
    r=2019
    cntYears=getCntYears()
    names=[str(x) for x in range(l,r)]
    #x=list(range(len(names)))
    y=[cntYears[i] for i in range(l,r)]
    line = Line("水利厅历年发文量")
    #line.add("", attr, v1, mark_point=["average"])
    line.add("", names, y,is_fill=True,area_color="#000", mark_point=["max", "min"], mark_line=["max", "average"])
    line.render()
    return line
def showHotRankOfCity():
    ans=getEchartsK()
    kline = Kline("各城市发文K线图")
    kline.add(
            "",
            list(ans.keys()),
            list(ans.values()),
            mark_point=["min"],
            is_datazoom_show=True,
            #datazoom_orient="vertical",
            )
    kline.render()
def showEmotionByQ():
    dictM=getEmotionDictM()
    bar=Bar("各个季度情感指数")
    bar.add("",list(dictM['季度']),list(dictM['情感指数']))
    bar.render()
    return bar
def showHotWords():
    hotWords=getHotWordsData()
    line=Line("历年水利热词变化")
    dates=[item.strftime("%Y%m") for item in hotWords.index]
    for item in hotWords:
        line.add(item,dates,list(hotWords[item]))
    line.render()
    return line

def showHotHuman():
    hotWords=getHotHumanData()
    line=Line("历年水利人物图壹")
    dates=[item.strftime("%Y%m") for item in hotWords.index]
    for item in hotWords:
        line.add(item,dates,list(hotWords[item]))
    line.render()
    return line
def showHotHuman1():
    hotWords=getHotHumanData1()
    line=Line("历年水利人物图壹")
    dates=[item.strftime("%Y%m") for item in hotWords.index]
    for item in hotWords:
        line.add(item,dates,list(hotWords[item]))
    line.render()
    return line
