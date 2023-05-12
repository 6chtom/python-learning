"""
列表推导式(II) 
高级推导式 1 ：
["expression" "for target in iterable" "if condition"]

列表推导式的条件判断
先运行中间遍历，再运行条件语句，最后运行expression表达式
"""

# 循环创建二维列表
matrix = [0] * 3
for i in range(len(matrix)):
    matrix[i] = [0] * 3
print(matrix)         # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 列表推导式创建二维列表
matrix = [[0] * 3 for i in range(3)]
print(matrix)         # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 高级推导式
even_number = [i for i in range(10) if i % 2 == 0]
print(even_number)              # [0, 2, 4, 6, 8]


words = ["Great", "FishC", "Brilliant", "Excellent", "Fantastic"]
F_Beginning_Words = [w for w in words if w[0] == 'F']
print(F_Beginning_Words)        # ['FishC', 'Fantastic']

"""
高级推导式 2 ：
[expression for target1 in iterable1
            for target2 in iterable2
                       ...
            for targetN in iterableN]

列表推导式的多层嵌套
依次执行target1 → target2 → ··· → targetN
"""

# 二维列表的展开（二向箔打击）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [col for row in matrix for col in row]
print(flatten)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 可以理解为先展开row，再在每一个row展开col依次输出

# 写成循环可以是
flatten = []
for row in matrix:
    for col in row:
        flatten.append(col)
print(flatten)

_ = [x + y for x in "fishc" for y in "FISHC"]
print(_)
# ['fF', 'fI', 'fS', 'fH', 'fC', 'iF', 'iI', 'iS', 'iH', 'iC', 'sF', 'sI', 'sS', 'sH', 'sC', 'hF', 'hI', 'hS', 'hH', 'hC', 'cF', 'cI', 'cS', 'cH', 'cC']
#理解为依次拼接（笛卡尔乘积）

# 写成循环
_ = []     # 无关紧要的变量可以直接用下划线 _ 代替
for x in "fishc":
    for y in "FISHC":
        _.append(x + y)
print(_)
# ['fF', 'fI', 'fS', 'fH', 'fC', 'iF', 'iI', 'iS', 'iH', 'iC', 'sF', 'sI', 'sS', 'sH', 'sC', 'hF', 'hI', 'hS', 'hH', 'hC', 'cF', 'cI', 'cS', 'cH', 'cC']

"""
高级（终极）推导式 3 ：
[expression for target1 in iterable1 if condition1
            for target2 in iterable2 if condition2
                             ...
            for targetN in iterableN if conditionN]

尽量不要过分复杂
"""

_ = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(_)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6], [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]

_ = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                _.append([x,y])
print(_)
# [[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6], [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]


