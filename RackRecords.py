# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:19:59 2021

@author: Renyu_Qbebee
"""

import pymysql,datetime,numpy,locale,logging
import os
#str='2021-04-03'.__format__('%y-%m-%d')

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",filename='records.log')
logging.info("program starting...")
print("程序启动......")
locale.setlocale(locale.LC_ALL,'')
db = pymysql.connect(user='root',passwd='root',host='localhost',database='mydb',port=3306,use_unicode=True)
cursor = db.cursor()
fq= str(datetime.date.today())
cursor.execute('select count(*)from gondan_6m')
db.commit()
result=int(cursor.fetchone()[0])    #记录条数
if result==None or result==0:
    result=0

sanj=0
temp=0
persons=int(eval(input("今日翻堆开工人数: ")))
if persons >1 :
    for person in range(persons):
        print("开始录入第%d人的翻堆数据......"%(person+1))
        name=input("姓名: ")
        bans=int(input("板数: "))
        sanj2=input("散件: ")
        sanj=0;
        if sanj2!=None and sanj2!='' and len(str(sanj2).split(','))>1:
            sanjs=str(sanj2).split(',')
            #重新调整整板板数及散件数
            for sj in sanjs:
                temp+=int(eval(sj))
            if temp>=198:
                bans2=bans
                bans=bans+temp//198
                sanj=temp%198
            else:
                bans2=bans
                sanj=temp
        else:
            bans2=bans
            if sanj2==None or sanj2=='':
                sanj=0
            else:
                sanj=int(sanj2)
        id = result+1     #记录ID
        print(id,fq,name,bans,sanj,bans2,sanj2)
        sqlstr="insert into mydb.gondan_7m(fadriq,name,bans,sanj,bans2,sanj2) values('%s','%s','%d','%d','%d','%s')"%(fq,name,bans,sanj,bans2,sanj2)
        cursor.execute(sqlstr)
        db.commit()
        print("成功插入第%d条数据到后台数据库"%(person+1))
        print("")
        sanj=0
        temp=0
elif persons==1:
    name=input("姓名:")
    bans=int(input("板数:"))
    sanj2=input("散件:")
    sanj=0;
    if sanj2!= None and sanj2 != '' and len(str(sanj2).split(',')) > 1:
        sanjs = str(sanj2).split(',')
        temp = 0
        #重新调整整板板数及散件数
        for sj in sanjs:
            temp += int(eval(sj))
        if temp >= 198:
            bans2=bans
            bans = bans + temp // 198
            sanj = temp % 198
        else:     #例如24,66,49
            bans2 = bans
            sanj=temp
        temp = 0
    else:
        bans2 = bans
        if sanj2==None or sanj2=='':
            sanj=0
        else:
            sanj = int(sanj2)
    id = result+1     #记录ID
    print(id,fq,name,bans,sanj,bans2,sanj2)
    sqlstr = "insert into mydb.gondan_7m(fadriq,name,bans,sanj,bans2,sanj2) values( '%s','%s','%d','%d','%d','%s')"%(fq,name,bans,sanj,bans2,sanj2)
    try:
        cursor.execute(sqlstr)
        db.commit()#这里提交操作这一步很重要
        print("数据提交入库成功!")
    except Exception:
        print("出错啦")
elif persons==0 or persons is None:
    print("今天无需录入翻堆数据，厂方未指派生产任务。")
else:
    print("翻堆人数输入有误，请重新输入！")
print("今天总共%d人翻堆, 作业数据录入完毕。"%persons)
#查验一下当天录入的数据是否有重复或漏记
cursor.execute("select * from gondan_7m where fadriq ='%s'"%fq)
db.commit()
print("")
print("今天录入的数据如下,请仔细核对！")
todayRecords = cursor.fetchall()
for ts in todayRecords:
    print(ts)
#cursor.close()   
print('')
print('7月份翻堆组个人累计数据汇总如下：')
cursor.execute('select name ,count(name),sum(bans),sum(sanj) from gondan_7m group by name order by fadriq')
db.commit()
result = cursor.fetchall()
bans_total=0
sanj_total=0
for rt in result:
    if int(rt[3])>=198:
        bans_total=int(rt[2])+int(rt[3])//198
        sanj_total=int(rt[3])%198
    else:
        bans_total=rt[2]
        sanj_total=rt[3]
    print("||%s:出勤%d天,共%d板,另加%d件."%(rt[0],rt[1],bans_total,sanj_total))
    
print("")
for rs in result:
    print(rs)

    
print("今日所有翻堆数据均已成功入库，程序结束。")
logging.info("Program is over. Later this windows should be close.")
cursor.close()
db.close()
