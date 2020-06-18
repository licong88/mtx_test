import random
# 玩家出拳
# 0-石头，1-剪刀，2-布
num_relation = ['石头', '剪刀', '布']
count = {'win': 0, 'ping': 0, 'lose': 0}

while True:
    p = input('请玩家出拳（0-石头，1-剪刀，2-布, q/Q-退出）： ')
    if p in ['0', '1', '2']:
        p = int(p)
        # 电脑出拳方式
        c = random.randint(0,2)
        print('玩家:{} VS 电脑:{} '.format(num_relation[p], num_relation[c]))
        # 赢
        if (p==0 and c==1) or (p==1 and c==2) or (p==2 and c == 0):
            print('赢了')
            count['win'] += 1
        elif p == c:
            print('平局')
            count['ping'] += 1
        else:
            print('输了')
            count['lose'] += 1
    elif p in ['q', 'Q']:
        print('玩家总共玩了{}局，其中赢了{}局，平了{}局，输了{}局！'.format(count['win']+count['ping']+count['lose'], count['win'], count['ping'], count['lose']))
        break
    else:
        print('输入错误，请重新输入！')