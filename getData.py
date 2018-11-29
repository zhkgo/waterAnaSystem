# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql
def load_tot_table():
    db=pymysql.connect(host='localhost',user='root',password='19971206zhk.',port=3306,charset='utf8')
    cursor=db.cursor()
    cursor.execute('use news')
    cursor.execute("SELECT title,content,time,origin FROM cor")
    contents=cursor.fetchall()
    db.close()
    return contents
def load_titles():
    db=pymysql.connect(host='localhost',user='root',password='19971206zhk.',port=3306,charset='utf8')
    cursor=db.cursor()
    cursor.execute('use news')
    cursor.execute('SELECT title,time FROM articlelist')
    titles=cursor.fetchall()
    db.close()
    return titles

def load_content():
    db=pymysql.connect(host='localhost',user='root',password='19971206zhk.',port=3306,charset='utf8')
    cursor=db.cursor()
    cursor.execute('use news')
    cursor.execute("SELECT content FROM articles")
    contents=cursor.fetchall()
    db.close()
    return contents

