from encodings import utf_8


#_*_coding_*_ = utf_8
import datetime
import random
import win32com.client
sper = win32com.client.Dispatch("SAPI.Spvoice")
print("\n=============高考倒计时===================")
sper.Speak("高考倒计时")
now = datetime.datetime.today()
print("今天是: ",now.strftime("%Y-%m-%d %A %B %j %U"))
sper.Speak("今天是: %s"%now.strftime("%Y-%m-%d %A"))
time1 = datetime.datetime(2022,6,7)
time2 = datetime.datetime(2023,6,7)
print("距离2022年高考还有"+str((time1-now).days)+"天")
sper.Speak("距离2022年高考还有"+str((time1-now).days)+"天")
print("距离2023年高考还有"+str((time2-now).days)+"天")
sper.Speak("距离2023年高考还有"+str((time2-now).days)+"天")

clerks =["梁斌","尹小年","王晨阳","肖学军","王桂春","戴新型","仇静文","张德华","陈新道","蒋健","刘丰兵","罗艳红","彭炎青","彭荷花","陈义佩","胡建华"]
hongbao = [1,5,10,20,100]
for p in range(1,10):
    sper.Speak("%s 红包%d元"%(random.choice(clerks),hongbao[random.randint(0,4)]))

def is_valid(string):
    try:
        
        num = input("Please enter a number")
        if num.isdigit()==True:
            string = int(num)
            return True
    
        else:
            print("请重新输入有效数字")
    except (TypeError, ValueError):
        print("输入出错啦!")
        pass        