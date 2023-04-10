"""
改进建议：
1. 当用户猜错的时候，程序应该给出提示 √
2. 应该提供多次机会给用户 √
3. 每次运行程序，答案应该是随机的
"""

"""随机数random模块
1. 使用时需要引入random的模块
2. random.randint(100,10000)表示随机一个100到10000的整数(包含100)
"""

import random

counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("不妨猜一下我现在想的数字：")
    guess = int(temp)

    if guess == answer:
        print("你懂我")
        print("猜中也没奖励")
        break    # break只是用来跳出一层循环体，记住是一层
    else:
        if guess < answer:
            print("小了")
        else:
            print("大了")
        counts = counts -1

print("游戏结束，不玩了")