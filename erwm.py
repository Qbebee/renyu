import qrcode  
import matplotlib as plt  





#img = qrcode.make('hello qrcode !')
#img.save('test.png')
#img.show()


 
#text = input("输入文字或URL：")  # 设置URL必须添加http://
#img2 =qrcode.make(text)
#img2.save("d:/ryproject/qbebee.png")                            #保存图片至本地目录，可以设定路径
#img2.show()
qr = qrcode.QRCode(version=10,error_correction=qrcode.ERROR_CORRECT_M,box_size=10,border=2)
qr.add_data('仁宇齐碧碧')
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
#img = img.convert("RGBA")
#img.save("qbebee1.png")
img.show()
#erwm = qrcode.make('DWRK21718J4519162')
#erwm.save('DWRK21718J4519162.png')



"""
import Image
def getQRcode(strs, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    # 添加数据
    qr.add_data(strs)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="blue", back_color="white")
    img = img.convert("RGBA")  # RGBA
    # 添加logo
    icon = Image.open("321.png")
    # 获取图片的宽高
    img_w, img_h = img.size
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    print(icon)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)
    # 显示图片
    plt.imshow(img)
    plt.show()
    img.save(name)
    return img

if __name__ == '__main__':

    getQRcode("https://music.163.com/song?id=36990266&userid=112961323", '01.png')
"""
