"""
循环结构 while 和 for
"""

"""
while循环

while condition:
    statement(s)

"""
i = 1
sum = 0
while i <= 1000000:
    sum = sum + i     # sum += i
    i = i + 1         # i += 1
print(sum)

"""
break语句
break，跳出一层循环
"""
while True:
    answer = input('主人，我可以退出循环了吗？')
    if answer == '可以':
        break
    print('哎，好累')
