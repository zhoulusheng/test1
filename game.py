import time,random
# 初始化对局
player_victory = 0
enemy_victory =0
# 循环对局
for i in range(1,4):
    time.sleep(1)
    print('现在开始第'+str(i)+'局')
# 生成双方角色并随机生成属性
# 生成双方角色并随机生成属性
    player_life = random.randint(100,150)
    player_attack = random.randint(30,50)
    enemy_life = random.randint(100,150)
    enemy_attack = random.randint(30,50)
# 展示双方属性
    print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
    print('----------------------')
    time.sleep(1)
    print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
    time.sleep(1)

# 双方PK
    while player_life >= 0 and enemy_life >= 0:
        player_life -= enemy_attack
        enemy_life -= player_attack
        print('你发起了攻击，【敌人】的血量：'+str(enemy_life))
        print('敌人发起了攻击，【玩家】的血量：'+str(player_life))
        print('------------------')
        time.sleep(1)


# 打印战果
    if player_life >= 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了！你赢了！')
    elif player_life <= 0 and enemy_life >= 0:
        enemy_victory += 1
        print('悲催！你被敌人干掉了！')
        print('-------------')
        time.sleep(1)
    else:
        print('你们同归于尽！')
if player_victory > enemy_victory:
    print(str(i)+'局'+str(player_victory)+'胜，你赢了！')
    time.sleep(1)
elif player_life < enemy_life:
    print(str(i)+'局'+str(enemy_victory)+'胜，敌人赢了！')
    time.sleep(1)
else:
    print('--------最终平局---------')
input('任意键退出')
