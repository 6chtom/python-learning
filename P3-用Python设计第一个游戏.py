"""P3-用Python设计第一个游戏"""
"""用Python设计第一个游戏"""

temp = input("不妨猜一下我现在想的数字：")
guess = int(temp)

if guess == 8:
    print("你懂我")
    print("猜中也没奖励")
else:
    print("猜错咯")

print("游戏结束，不玩了")