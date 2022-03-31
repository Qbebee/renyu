# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:19:59 2021

@author: Renyu_Qbebee
"""

import pymysql,datetime,numpy,locale,logging,math
import os
#str='2021-04-03'.__format__('%y-%m-%d')

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",filename='records_2203m.log')
logger =logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.log(logging.INFO,'程序启动.......')
#logger.log(logging.DEBUG,'DEBUG 信息')
#logger.log(logging.INFO,'INFO信息')
#logger.log(logging.WARNING,'WARNING 信息')
logger.addHandler(logging.FileHandler('errors.log'))
#logger.log(logging.ERROR,'ERROR 信息')
#logger.log(logging.CRITICAL,'CRITICAL 信息')


logging.info("program starting...")
print("程序启动......")
locale.setlocale(locale.LC_ALL,'')
db = pymysql.connect(user='root',passwd='root',host='localhost',database='mydb',port=3306,use_unicode=True)
cursor = db.cursor()
fq= str(datetime.date.today())
logger.log(logging.INFO,'%s开始数据录入业务操作。'%fq)
cursor.execute("select count(*)from gondan_202203m where fadriq = '%s'"%fq)
db.commit()
result=int(cursor.fetchone()[0])    #记录条数
if result==None or result==0:
    result=0
    print("今天尚未录入任何生产数据！")
    logger.log(logging.WARNING,"今天尚未录入任何生产数据！")
    

sanj=0
temp=0
try:
    persons=int(eval(input("今日翻堆开工人数: ")))
except NameError as err1:
    print('输入非数字错误：'+err1.__str__())
    logger.log(logging.ERROR,'ERROR 信息'+err1.__str__())
except ValueError as err2:
    print('输入错误：'+err2.__str__())    
        
if math.isfinite(persons)==False:
    print("输入了非数字字符，请重新输入！")
    
if persons >1 :
    for person in range(persons):
        print("开始录入第%d人的翻堆数据......"%(person+1))
        logger.log(logging.INFO,"开始录入第%d人的翻堆数据......"%(person+1))
        
        name=input("姓名: ")
        logger.log(logging.INFO,"姓名：%s"%name)
        bans=int(input("板数: "))
        logger.log(logging.INFO,"板数：%d"%bans)
        sanj2=input("散件: ")
        logger.log(logging.INFO,"散件：%s"%sanj2)
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
        print(person+1,fq,name,bans,sanj,bans2,sanj2)
        logger.log(logging.INFO,'记录信息：||%d ||%s ||%s ||%d ||%d ||%d ||%s||'%(person+1,fq,name,bans,sanj,bans2,sanj2))
        sqlstr="insert into mydb.gondan_202203m(fadriq,name,bans,sanj,bans2,sanj2,totals) values('%s','%s','%d','%d','%d','%s','%d')"%(fq,name,bans,sanj,bans2,sanj2,int(int(bans)*198+int(sanj)))
        cursor.execute(sqlstr)
        db.commit()
        print("成功插入第%d条数据到后台数据库"%(person+1))
        logger.log(logging.INFO,"成功插入第%d条数据到后台数据库"%(person+1))
        print("")
        sanj=0
        temp=0
elif persons==1:
    name=input("姓名: ")
    logger.log(logging.INFO,"姓名：%s"%name)
    bans=int(input("板数: "))
    logger.log(logging.INFO,"板数：%d"%bans)
    sanj2=input("散件: ")
    logger.log(logging.INFO,"散件：%s"%sanj2)
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
    print(persons,fq,name,bans,sanj,bans2,sanj2)
    logger.log(logging.INFO,'记录信息：||%d ||%s ||%s ||%d ||%d ||%d ||%s||'%(persons,fq,name,bans,sanj,bans2,sanj2))
    sqlstr = "insert into mydb.gondan_202203m(fadriq,name,bans,sanj,bans2,sanj2,totals) values( '%s','%s','%d','%d','%d','%s','%d')"%(fq,name,bans,sanj,bans2,sanj2,int(int(bans)*198+int(sanj)))
    try:
        cursor.execute(sqlstr)
        db.commit()#这里提交操作这一步很重要
        print("数据提交入库成功!")
        logger.log(logging.INFO,"数据提交入库成功!")
    except Exception:
        print("出错啦")
        logger.log(logging.ERROR,"数据提交数据库操作出错了")
    print("今天总共%d人翻堆, 作业数据录入完毕。"%persons)
    logger.log(logging.INFO,"今天总共%d人翻堆, 作业数据录入完毕。"%persons)
elif (persons==0 or persons is None) and result==0:
    print("今天无需录入翻堆数据，厂方未指派生产任务。")
elif persons==0 and result>0:
    print("已录入生产数据,请勿重复!")    
else:
    print("翻堆人数输入有误，请重新输入！")

#查验一下当天录入的数据是否有重复或漏记
cursor.execute("select * from gondan_202203m where fadriq ='%s'"%fq)
db.commit()
print("")
print("今天录入的数据如下,请仔细核对！")
logger.log(logging.INFO,"今天录入的数据如下,请仔细核对！")
todayRecords = cursor.fetchall()
daily_total=[]
for ts in todayRecords:
    daily_total.append(ts[7])
    print(ts)
    logger.log(logging.INFO,ts)
#统计个人总件数    
daily_totals =0
for dt in daily_total:
    daily_totals+=int(dt)
print("今天个人总件数合计：%d件。"%daily_totals)
logger.log(logging.INFO,"今天个人总件数合计：%d件。"%daily_totals)
daily_totals =0
       
#cursor.close()   
print('')
print('2022年3月份翻堆组个人累计数据汇总如下：')
logger.log(logging.INFO,"2022年3月份翻堆组个人累计数据汇总如下：")
cursor.execute('select name ,count(name),sum(bans),sum(sanj),sum(totals) from gondan_202203m group by name order by fadriq')
db.commit()
result = cursor.fetchall()
bans_total=0
sanj_total=0
ttotal=[]
for rt in result:
    if int(rt[3])>=198:
        bans_total=int(rt[2])+int(rt[3])//198
        sanj_total=int(rt[3])%198
    else:
        bans_total=rt[2]
        sanj_total=rt[3]
    ttotal.append(rt[4])  
    print("||%s:出勤%d天,共%d板,另加%d件,总共%d件."%(rt[0],rt[1],bans_total,sanj_total,rt[4]))
    logger.log(logging.INFO,"||%s:出勤%d天,共%d板,另加%d件,总共%d件."%(rt[0],rt[1],bans_total,sanj_total,rt[4]))
    
print("")
for rs in result:
    print(rs)
    logger.log(logging.INFO,rs)
#统计累计总件数    
ttl=0    
for mt in ttotal:
    ttl+= int(mt)    
print("本月累计总件数：%d件。"%ttl)
logger.log(logging.INFO,"本月累计总件数：%d件。"%ttl)
ttl=0

    
print("今日所有翻堆数据均已成功入库，程序结束。")
logger.log(logging.INFO,"今日所有翻堆数据均已成功入库，程序结束。")
logger.log(logging.INFO,"Program is over. Later this windows should be close.")


cursor.close()
db.close()
