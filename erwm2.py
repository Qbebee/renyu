#_*_coding=UTF8 -*-
from segno import helpers
qr =  helpers.make_mecard(
    name = "刘健全",
    nickname='齐碧碧',
    birthday="1974-11-14",
    phone='0738-8312053',
    videophone="18390840220",
    email='liujq417119@outlook.com',
    city='娄底',
    memo="娄底市水利水电工程建设有限公司",
    url="长沙市望城仁宇劳务服务有限公司",
    reading="湖南工商大学",
    roomno="长沙望城桂芳佳园小区5栋一单元1101室",
    prefecture="求仁得仁,恕己则已",
    zipcode='417000',
    country='中国'
)
qr.save('qebeemp.png',scale=10)

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open(r'hh.txt',"r").read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud


# 1.读入txt文本数据
text = open(r'hh.txt', "r").read()
#print(text)
# 2.结巴中文分词，生成字符串，默认精确模式，如果不通过分词，无法直接生成正确的中文词云
cut_text = jieba.cut(text)
# print(type(cut_text))
# 必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
result = " ".join(cut_text)
#print(result)
# 3.生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
# 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
wc = WordCloud(
        # 设置字体，不指定就会出现乱码
        # 设置背景色
        background_color='white',
        # 设置背景宽
        width=500,
        # 设置背景高
        height=350,
        # 最大字体
        max_font_size=50,
        # 最小字体
        min_font_size=10,
        mode='RGBA'
        #colormap='pink'
        )
# 产生词云
wc.generate(result)
# 保存图片
wc.to_file(r"wordcloud.png") # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
# 4.显示图片
# 指定所绘图名称
plt.figure("jay")
# 以图片的形式显示词云
plt.imshow(wc)
# 关闭图像坐标系
plt.axis("off")
plt.show()
#————————————————
#版权声明：本文为CSDN博主「半吊子全栈工匠」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/wireless_com/article/details/60571394