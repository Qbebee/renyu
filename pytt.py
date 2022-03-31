
import os
#import xlwings as xw
d1={"流水号":22031301,"翻堆日期":"20220313","姓名":"黄伟林","板数":40,"散件数":0}
d2={"流水号":22031302,"翻堆日期":"20220313","姓名":"瞿明","板数":48,"散件数":66}
d3={"流水号":22031303,"翻堆日期":"20220313","姓名":"盛文明","板数":39,"散件数":69}
    
for d in d1:
    print(d +" : "+str(d1[d]))
a = d2.items()
print(a)  
path = os.getcwd()
print(path)
file_list = os.listdir(path)
print(file_list)
for f in file_list:
    print(f)


"""
app = xw.App(visible=True,add_book=False)
workbook = app.books.add()
workbook.save("d:\\gondan.xlsx")
workbook.close()
app.quit()
    
"""   

import pandas as pd
s = pd.Series(["刘健全","刘国亮","刘振良","盛文明","瞿明","黄伟林","周振兴"])
print(s)
print("\n========================================================\n")
aa = pd.DataFrame([["20220313",39,69],["20220313",40,0],["      20220313",48,66]],
                  columns=["翻堆日期","板数","散件数"],
                  index=['盛文明','黄伟林','瞿  明'])
aa.index.name = "操作工"
print(aa)
print("\n========================================================\n")
df1 = pd.DataFrame({'操作工':['盛文明','黄伟林','       瞿  明'],'板数':[39,40,48],'散件数':[69,0,66]})
print(df1)
print("\n========================================================\n")
