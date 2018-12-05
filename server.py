# coding=utf8
from __future__ import unicode_literals

import random
import datetime

from flask import Flask, render_template
from flask.templating import Environment

from pyecharts import HeatMap, Map
from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig
from dataEcharts import *

# ----- Adapter ---------
class FlaskEchartsEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super(FlaskEchartsEnvironment, self).__init__(*args, **kwargs)
        self.pyecharts_config = PyEchartsConfig(jshost='/static/js')
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)


# ---User Code ----

class MyFlask(Flask):
    jinja_environment = FlaskEchartsEnvironment


app = MyFlask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/line1/")
def line1map():
	hm=showNewsYear()
	name='水利厅历年发文量'
	return render_template('echarts.html', name=name,hm=hm)
@app.route("/line2/")
def line2map():
	hm=showHotHuman()
	name='历年水利人物图壹'
	return render_template('echarts.html', name=name,hm=hm)
@app.route("/line3/")
def line3map():
	hm=showHotHuman1()
	name='历年水利人物图贰'
	return render_template('echarts.html', name=name,hm=hm)

@app.route("/bar1/")
def bar1map():
	hm=showCountry()
	name='排名前十的县级市'
	return render_template('echarts.html', name=name,hm=hm)
@app.route("/bar2/")
def bar2map():
	hm=showCitys()
	name='排名前十的地级市'
	return render_template('echarts.html', name=name,hm=hm)
@app.route("/bar3/")
def bar3map():
	hm=showEmotionByQ()
	name='各个季度情感指数'
	return render_template('echarts.html', name=name,hm=hm)

@app.route('/wordcloud1/')
def wordcloud1():
	name='做一个标题党专属的词云'
	src='https://wateranalysis-1252419034.cos.ap-shanghai.myqcloud.com/titleCloud.png'
	return render_template('pics.html', name=name,src=src)

@app.route('/wordcloud2/')
def wordcloud2():
	name='从全文内容来看关键词'
	src='https://wateranalysis-1252419034.cos.ap-shanghai.myqcloud.com/contentsCloud.png'
	return render_template('pics.html',name=name,src=src)
@app.route("/hotmap1/")
def hotmap1():
	hm=showHotMap()
	name='浙江各地发文数量热点图'
	return render_template('echarts.html', name=name,hm=hm)
@app.route("/hotmap2/")
def hotmap2():
	hm=showHotMap2()
	name='相关新闻最具影响力的县级市'
	return render_template('echarts.html', name=name,hm=hm)
@app.route("/box1/")
def box1map():
	src='https://wateranalysis-1252419034.cos.ap-shanghai.myqcloud.com/snspic.png'
	name='从盒图来看各地热度'
	return render_template('pics.html', name=name,src=src)
@app.route("/pie1/")
def pie1map():
	hm=showHotPie()
	name='热点词的对比'
	return render_template('echarts.html', name=name,hm=hm)
@app.route("/chra1/")
def chra1():
	return "暂时不能使用"
@app.route("/chra2/")
def chra2():
	return "暂时不能使用"
app.run(port=10086)
