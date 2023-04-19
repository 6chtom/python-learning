"""
continue 语句退出循环体
绕过这一次循环，进入下一次循环
"""
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

"""
while循环内的else，★★当循环条件不再为真的时候，执行else内的指令★★

while condition:
    statement(s1)
else:
    statement(s2)

"""
i = 1
while i < 5:
    print(f'循环内,i的值是{i}')
    if i == 2:
        break
    i += 1
else:
    print('i的值大于等于5')

day = 1
while day <= 7:
    answer = input("今天有好好学习吗？")
    if answer != "有":
        break
    day += 1
else:                                   # ★★当循环条件不再为真的时候，才执行else内的指令★★
    print("不错！7天全勤！")


"""
while循环结构的嵌套
"""
# 打印乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i}×{j}={i*j}", end = "\t")      # print语句如果结尾有特殊要求，需要添加end参数。\t 制表符更整齐美观
        j += 1
    else:
        print(end = "\n")     # 或者直接打印print()，这个作用就是换行
    i += 1
