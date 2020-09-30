import random
# 玩家出拳
player = int(input("请输入您要输出的拳头   石头(1)  剪刀(2)   布(3):"))
# 电脑出拳

# 随机数
computer = random.randint(1, 3)


print("玩家出的拳头是%s,电脑出的拳头是%s"%(player, computer))

if(player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer ==1):
    print("玩家赢了")
elif player == computer:
    print("平局")
else:
    print("电脑赢了")