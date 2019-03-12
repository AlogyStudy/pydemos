
import itchat
import math
import os
import PIL.Image as Image
import sys
import re

'''
获取微信用户性别
'''
def get_firend_sex(friend):
    # 初始化计数器
    male = female = other = 0
    # friend[0]是自己的信息，所以要从friends[1]开始
    for i in friend[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other +=1
    # 计算朋友总数
    total = len(friend[1:])
    print('好友总数：%s' % (str(total)) + '\n')
    print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
    "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
    "不明性别好友： %.2f%%" % (float(other) / total * 100))

'''
    获取签名
'''
def get_sign(friend):
    siglist = []
    for i in friend:
        signature = i['Signature'].strip().replace('span', '').replace('class', '').replace('emoji', '')
        rep = re.compile(r'1f\d+\w*|[<>/=]')
        signature = rep.sub('', signature)
        siglist.append(signature)
    text = ''.join(siglist)
    return text

'''
    微信用户头像拼接
'''

def main ():
    itchat.auto_login()

    # 获取用户名
    friend = itchat.get_friends(update=True)[0:]
    # user = friend[0]['UserName']

    # 获取性别
    get_firend_sex(friend)
    # 获取签名
    sign = get_sign(friend)

    
    num = 0

    # 获取用户头像
    for i in friend:
        img = itchat.get_head_img(userName=i['UserName'])
        with open('img' + '/' + str(num) + '.jpg', 'wb') as f:
            f.writa(img)
        num += 1
    
    ls = os.listdir('img')
    # # 计算大小
    each_size = int(math.sqrt(float(640 * 640) / len(ls)))
    lines = int(640 / each_size)
    image = Image.new('RGBA', (640, 640))
    x = 0
    y = 0

    # 每一张写入新图片
    for i in range(0, len(ls) + 1):
        try:
            img = Image.open('img' + '/' + str(i) + '.jpg')
        except IOError:
            print('Error')
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))
            x += 1
            if x == lines:
                x = 0
                y += 1
    # # 保存
    image.save('img' + '/' + 'all.jpg')
    itchat.send_image('img' + '/' + 'all.jpg', 'filehelper')

if __name__ == '__main__':
    main()
