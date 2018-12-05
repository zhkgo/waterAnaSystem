#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataWranging import *
from pyecharts import HeatMap, Map,Style,Pie,Kline
from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig
from pyecharts import Bar, Line, Grid
from pyecharts import Geo


def showCountry():
    labels,values=getCountryData()
    bar = Bar("提及次数前十")
    #其他主题：vintage,macarons,infographic,shine，roma 
  #  bar.use_theme("shine")
    bar.add("",labels[-10:],values[-10:],is_stack=True)
    bar.xaxis_name='县级市'
    bar.yaxis_name='提及次数'
    #bar.render()
    return bar
def showHotMap():
    attr,value,geo_cities_coords=getHotMapData()
    style = Style(title_color= "#fff",title_pos = "center",width =800,height = 600,background_color = "#132F3D")
    geo = Geo('浙江水利厅发文热力图',**style.init_style)
    geo.add("",attr,value,visual_range=[0,8000],symbol_size=15,
        visual_text_color= "#fff",is_piecewise = True,
        is_visualmap= True,maptype = '浙江',
        geo_cities_coords=geo_cities_coords)
    #geo.add("", attr, value, type="effectScatter", is_random=True, maptype = '浙江',effect_scale=4,geo_cities_coords=geo_cities_coords)
    #geo.render('浙江水利厅发文热力图.html')
    return geo
def showHotMap2():
    attr,value,geo_cities_coords=getHotMapData2()
    style = Style(title_color= "#fff",title_pos = "center",width =800,height = 600,background_color = "#132F3D")
    geo = Geo('相关新闻最具影响力的县级市',**style.init_style)
    geo.add("", attr, value, type="effectScatter", is_random=True, maptype = '浙江',effect_scale=4,geo_cities_coords=geo_cities_coords)
    #geo.render('浙江水利厅发文热力图.html')
    return geo

def showCitys():
    labels,values=getCitysData()
    bar = Bar("提及次数前十")
    #其他主题：vintage,macarons,infographic,shine，roma 
   # bar.use_theme("infographic")
    bar.add("",labels[-10:],values[-10:],is_stack=True)
    bar.xaxis_name='地级市'
    bar.yaxis_name='提及次数'
    #bar.render()
    return bar

def showHotPie(keys=getHotWords()):
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
   # pie.render()
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
  #  line.render()
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
 #   kline.render()
    return kline
def showEmotionByQ():
    dictM=getEmotionDictM()
    bar=Bar("各个季度情感指数")
    bar.add("",list(dictM['季度']),list(dictM['情感指数']), is_convert=True)
    #bar.render()
    return bar
def showHotWords():
    hotWords=getHotWordsData()
    line=Line("历年水利热词变化")
    dates=[item.strftime("%Y%m") for item in hotWords.index]
    for item in hotWords:
        line.add(item,dates,list(hotWords[item]))
   # line.render()
    return line

def showHotHuman():
    hotWords=getHotHumanData()
    line=Line("历年水利人物图壹")
    dates=[item.strftime("%Y%m") for item in hotWords.index]
    for item in hotWords:
        line.add(item,dates,list(hotWords[item]))
    #line.render()
    return line
def showHotHuman1():
    hotWords=getHotHumanData1()
    line=Line("历年水利人物图贰")
    dates=[item.strftime("%Y%m") for item in hotWords.index]
    for item in hotWords:
        line.add(item,dates,list(hotWords[item]))
   # line.render()
    return line
def showHotValue(city,keys,dateStart,dateEnd):
    hotWords=getKeysInCity(keys,city,dateStart,dateEnd)
    line=Line(city+"相关折线图")
    dates=[item.strftime("%Y%m") for item in hotWords.index]
    for item in hotWords:
        line.add(item,dates,list(hotWords[item]))
    #line.render()
    return line
def test():
    showHotValue('绍兴',getHotWords()[:6],'2017','2018')
