
import random

import scipy as sp
from aip import AipSpeech


hb = [1,5,10,20,50,100,200,500,1000,2000]
clerks =['梁斌','尹小年','王晨阳','肖学军','王桂春','戴新型','张德华','彭炎青','彭荷花','罗国荣','蒋健','刘丰兵','杨建国','胡佳宾','陈新道','罗艳红','黄灿']

for i in range(1,22):
    print( '第%d次派发红包，%s的红包%d元已到账，请注意查收!'%(i,clerks[random.randint(0,14)],hb[random.randint(0,9)]))
    
com = '娄底市水利水电工程建设有限责任公司'
for word in com :
    print( word)
    
APP_ID = '0738'
API_ID = '8312053'
SECRET_KEY = '13607388745'
client = AipSpeech(APP_ID,API_ID,SECRET_KEY)
#result = client.synthesis('你好百度先生','zh',1,{'vol':5,'per':4})
  
import pyttsx3

eg =pyttsx3.init()
eg.say('Hello, world, How are you?')
eg.runAndWait()  

import win32com.client as win 

speak = win.Dispatch('SAPI.SpVoice')
speak.Speak('Where are you from?')
speak.Speak('你哪里人?')
speak.Speak('请注意，请注意，2022年新春开年红包随机派送开始啦，开始啦，请大家赶快到办公室来领取。')
speak.Speak(com)
for i in range(1,22):
    aaa = '第%d次派发红包，%s的红包%d元已到账，请注意查收!'%(i,clerks[random.randint(0,14)],hb[random.randint(0,9)])
    
    speak.Speak(aaa)
    print( aaa)

speak.Speak('2022年新春红包派送大会结束，谢谢大家!散会!')    
    