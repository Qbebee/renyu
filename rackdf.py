#_*_ coding=utf-8 _*_
import pandas as pd
import pymysql
from sqlalchemy import create_engine, engine

engine = create_engine('mysql+pymysql://root:root@localhost:3306/mydb')
conn = pymysql.connect(host='127.0.0.1', port=3306,user='root',password='root',database='mydb')
sql_str = "select id as '记录ID',fadriq as '翻堆日期',name as '姓名',bans as '板数',sanj as '散件数',totals as '总件数' from gondan_8m order by name,fadriq"
#result = pd.io.sql.read_sql_query(sql_str, engine)
sqlstr = 'select * from gondan_8m where name="刘健全" order by fadriq'
sql = 'select * from gondan_8m order by name,fadriq'
result = pd.read_sql_query(sqlstr, conn)

#print(type(result),'\n',result)
print(result)

#df=pd.read_csv(r'd:/ryproject/my_8m_gondan.csv')
#print(df)



