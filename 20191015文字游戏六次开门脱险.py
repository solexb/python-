import random

print('2019军运会期间武汉......')
print('凌晨三点又累又饿......')
print('因为加班被困在熊猫玩办公大楼中，这个时候你发现了一道不常用的非钥匙密码暗门')
print('门上锈迹斑驳，依稀可辨：此门需要2位密码开启，请输入0~100间的数字，如果猜对门会开启，注意每24小时只有6次机会。')
n = random.randint(0,100)
# 定义猜的总次数
count = 6
while True:
    ni = int(input(''))
    # -= 和 += 一样，是一个操作符，读作“减等”，先减再赋值，相当于count = count - 1
    # 每次猜，次数都减去1
    count -= 1
    # 如果没有次数了，则游戏结束
    if count == 0:
        print('疲劳和困倦加上厚重的门依然封闭，只能在这里等待第二天天亮......')
        print('游戏结束')
        break

    if ni > n:
        print('猜大了')
        print('你还剩%s次机会，门上闪动的红色信号显示又错了一次，失败的风险越来越高......' % count)
        continue
    elif ni < n:
        print('猜小了')
        print('你还剩%s次机会，门上闪动的红色信号显示又错了一次，失败的风险越来越高......' % count)
        continue
    else:
        print('猜对了，一声滋啦，门上绿灯闪烁，你逃离了加班密室！')
        break
    
