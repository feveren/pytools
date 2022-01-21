#!/usr/bin/python
# -*- coding: UTF-8 -*- 

from datetime import datetime

# 时间字符串转时间毫秒数
def toMicrosecond(time, format = "%Y-%m-%d %H:%M:%S.%f"):
    return datetime.strptime(time, format).timestamp()

# 格式化时间毫秒数
def formatDatetime(time, format = "%Y-%m-%d %H:%M:%S"):
    t = str(time)
    datetimeStr = datetime.fromtimestamp(int(t[:10])).strftime(format)
    if len(t) > 10:
        datetimeStr = "%s.%s" % (datetimeStr, t[10:])
    return datetimeStr

print(toMicrosecond("2017-10-11 09:29:30.777"))
print(formatDatetime("1507685370777"))

# ----------------------------------------------------

import re

# 正则表达式
def regix(line):
    matches = re.search(r'^\[(.*?)\].*?aos a?sync request.*?mId=\'(.*?)\'.*?mUrl=\'(.*?)\'', line)
    if not matches:
        return
    groups = matches.groups()
    time = groups[0]
    id = groups[1]
    url = groups[2]

def readFile(path):
    with open(path, "r") as log:
        while True:
            line = log.readline()
            if not line:
                break
            print(line)

# ----------------------------------------------------

import pandas

def parseCsv(path):
    df = pandas.read_csv(path, dtype={'clienttime': str}).copy()
    clienttime = df['clienttime']
    for index in range(len(clienttime)):
        clienttime[index] = formatDatetime(clienttime[index])
    df.to_csv(path, encoding='utf-8')

parseCsv("/Users/rentao/Downloads/弱网sql结果/W6uLJ4TiES8DAFhg3LK91aDh.csv")

