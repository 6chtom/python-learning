"""
改进建议：
1. 当用户猜错的时候，程序应该给出提示
2. 应该提供多次机会给用户
3. 每次运行程序，答案应该是随机的
"""

"""while循环语句
while 条件:
    如果条件为真(True)执行这里的语句
"""

temp = input("不妨猜一下我现在想的数字：")
guess = int(temp)

if guess == 8:
    print("你懂我")
    print("猜中也没奖励")
else:
    if guess < 8:
        print("小了")
    else:
        print("大了")

print("游戏结束，不玩了")