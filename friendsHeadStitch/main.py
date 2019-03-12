
import itchat
import math
import os
import PIL.Image as Image

'''
    微信用户头像拼接
'''

def main ():
    itchat.auto_login(enableCmdQR=True)

    # 获取用户名
    friend = itchat.get_firend(update=True)[0:]
    user = friend[0]['UserName']

    num = 0

    # 获取用户头像
    for i in friend:
        img = itchat.get_head_img(userName=i['UserName'])
        fileImage = open('文件夹' + '/' + str(num) + '.jpg', 'wb')
        fileImage.write(img)
        fileImage.close()
        num += 1
    
    ls = os.listdir('文件夹')
    # 计算大小
    each_size = int(math.sqrt(float(640 * 640) / len(ls)))
    lines = int(640 / each_size)
    image = Image.new('RGBA', (640, 604))
    x = 0
    y = 0

    # 每一张写入新图片
    for i in range(0, len(ls) + 1):
        try:
            img = Image.open('文件夹' + '/' + str(i) + '.jpg')
        except IOError:
            print('Error')
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))
            x += 1
            if x == lines:
                x = 0
                y += 1
    # 保存
    image.save('文件夹' + '/' + 'all.jpg')
    itchat.send_image('文件夹' + '/' + 'all.jpg', 'filehelper')

if __name__ == '__main__':
    main()
