# -*- coding: utf8 -*-

import matplotlib.pyplot as plt

font1 = {'family' : 'SimSun',
'weight' : 'normal',
'size'   : 20,
}
labels = [u'刘健全', u'瞿明', u'盛文明', u'黄伟林',u'刘振良',u'刘国亮']
sizes=[0.1827 ,0.2646 ,0.1296 ,0.2052 ,0.0790 ,0.1389]
explode = [0.08,0,0,0,0,0]
colors = [u'red',u'blue',u'yellow',u'pink',u'purple',u'gray']
patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   labeldistance=1.1, autopct='%2.0f%%', shadow=False,
                                   startangle=90, pctdistance=0.6,textprops=font1)
# # 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.title(label='2022年6月仁宇大旺翻堆组产量占比',fontdict=font1,loc='center')
plt.grid()
plt.show()