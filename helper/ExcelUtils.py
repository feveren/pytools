#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import pandas

def parseCsv(path):
    df = pandas.read_csv(path, dtype={'clienttime': str}).copy()
    clienttime = df['clienttime']
    for index in range(len(clienttime)):
        clienttime[index] = formatDatetime(clienttime[index])
    df.to_csv(path, encoding='utf-8')

parseCsv("/Users/rentao/Downloads/弱网sql结果/WGfWAwfhakDAO6qWNVqrCQp.csv")

