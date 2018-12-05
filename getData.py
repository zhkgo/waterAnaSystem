# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
def loadTotTable():
    db=pymysql.connect(host='localhost',user='root',password='19971206zhk.',port=3306,charset='utf8')
    cursor=db.cursor()
    cursor.execute('use news')
    cursor.execute("SELECT title,content,time,origin FROM cor")
    contents=cursor.fetchall()
    db.close()
    return contents
def loadTitles():
    db=pymysql.connect(host='localhost',user='root',password='19971206zhk.',port=3306,charset='utf8')
    cursor=db.cursor()
    cursor.execute('use news')
    cursor.execute('SELECT title,time FROM articlelist')
    titles=cursor.fetchall()
    db.close()
    return titles

def loadContent():
    db=pymysql.connect(host='localhost',user='root',password='19971206zhk.',port=3306,charset='utf8')
    cursor=db.cursor()
    cursor.execute('use news')
    cursor.execute("SELECT content FROM articles")
    contents=cursor.fetchall()
    db.close()
    return contents

