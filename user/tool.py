import os
import xlrd
import json
import re


def verifyPhone(phone):
    try:
        r = r'^(0|86|17951)?(13[0-9]|15[012356789]|17[013678]|18[0-9]|14[57])[0-9]{8}$'
        a = int(phone)
        if re.match(r, str(a)):
            return True
        else:
            return False
    except:
        return False


def verifyName(name):
    isPhone = verifyPhone(name)
    if len(name)>1 and not isPhone:
        return True
    else:
        return False

def formatData(datas,code,msg):
    dictMerged = {
        "code":code,
        "msg":msg
    }
    if datas:
        dictMerged['data'] = datas
    return dictMerged


def loadxl(path):
    resultDict = None
    try:
        data = xlrd.open_workbook(path)
        allData = []
        for table in data.sheets():
            nrows = table.nrows
            ncols = table.ncols #列数
            arrDict = []
            for i in range(nrows):
                phone = ""
                name = ""
                for data in table.row_values(i):
                    if verifyPhone(data):
                        phone = data
                    if verifyName(str(data)):
                        name = data
                if name and phone:
                    dict = {'name':name,'phone':phone}
                    arrDict.append(dict)
            allData += arrDict
            resultDict = formatData(allData,200,'success')
    except:
        resultDict = formatData(None,500,'文件格式不正确')

    return resultDict