print('熊猫玩大楼，一个2009年落成的建筑。距今已经10年。游戏之魂世世代代凝聚在这里。到熊猫玩一派继承此地这年，已经整整一年。也就是这一年，建筑物里面突然出现了很多奇怪的人，到晚上更是妖风四起，邪魅横行。\n')
print('solex的式神为了查出事情的真相，乔装打扮混进了公司大楼，隐匿在角落苦练嫁衣神功，然而这一去竟然杳无音信。一年之后，solex收到了一封信，上面就写了画了一双筷子：“暗语快走”\n')
print('solex感觉到了事情的严重性，就带着行李和宠物旺财，小强，还有绿植，在某天的拂晓时分悄悄离开了熊猫玩大楼，走了不知道多久，再也跑不动了，就在武汉江南家园一偏僻的二单元隐居了起来。\n')
print('这一隐就是16个月。这16个月间，solex也变成了一个高级的社会人。\n')
print('为了探寻熊猫玩大楼式神失踪的真相，为了带返思念熊猫玩大楼的旺财，小强重新回到大楼生活。在这一天清晨，solex带着祖上传下来的————仿神农鼎式神炉，关上大门，告别绿植宠物，只身一人开始了自己的冒险之旅。\n')
print('从记事起，这套式神居的祖传香炉就一直在家里的角落里面陪着solex。这几天不知道为什么，经常自己在寒冷中发出铿铿作响，solex觉得救自己人的时机来了，炉中仙和式神在共鸣，这也是solex决定出来的原因。\n')
print('solex打听到，当年那些奇怪的人都是下界的妖怪异兽，现在整个熊猫玩大楼方圆5米都被妖兽所侵染，而妖兽的总部就在熊猫玩4楼！！\n')
print('solex千辛万苦，历经无数磨难，终于抵达了熊猫玩4楼，见到了最终大BOSS————周鹏。\n')
print('游戏规则：BOSS有10点血，每次攻击，减一点血，打10次，他就昏迷气绝并归还你的式神。\n')
print('\n')
import random
print('欢迎跳转熊猫玩大楼群熊塔，如今是妖兽大本营')
print('历经九死一生，你来到了Boss周鹏的老巢\n')
hp_boss = 30
print('周鹏血量:',hp_boss,'准备开始战斗！！')
while True:
    input_ni = int(input("输入数字1攻击！"))
    if input_ni == 1:
        # 表示solex打出的随机伤害，伤害值为3~5之间的数，包括3和5
        attack_player = random.randint(3,5)
        hp_boss -= attack_player # Boss血量根据随机攻击值扣除
        print('你击中了周鹏，打出了',attack_player,'的伤害，周鹏剩余血量',hp_boss)
        if hp_boss <= 0:
            print("Hero,恭喜你，击败了最终BOSS周鹏，式神苏为奴获救！")
            break   # 结束死循环
    else:
        print('攻击无效，请使用大宝剑攻击，按数字1')    
        
        
