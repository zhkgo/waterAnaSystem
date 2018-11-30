#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
pathOfHotWords="keywords/hot.txt"
pathOfReligions="keywords/citys.xls"
pathOfHuman="keywords/human.txt"
pathOfHuman1="keywords/human1.txt"
pathOfMap="keywords/latAndLon.xls"
#
def getTXT(filename):
    with open(filename,"r") as f:
        words=f.read().split()
    return words
def getHotWords():
    return getTXT(pathOfHotWords)
def getReligions():
    return pd.read_excel(pathOfReligions)
def getHuman():
    return getTXT(pathOfHuman)
def getHuman1():
    return getTXT(pathOfHuman1)
def getPosition():
    return pd.read_excel(pathOfMap)