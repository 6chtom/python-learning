"""
列表推导式:
[expression for target in iterable]

用来统一修改或生成列表中的数据，输出的是列表
很高效，必须掌握
"""

# 写一个程序，使得每一个元素都是初始元素的2倍
num_1 = [1, 2, 3, 4, 5]
for i in range(len(num_1)):
    num_1[i] = num_1[i] * 2
print(num_1)         # [2, 4, 6, 8, 10]
# 比较繁琐，需要很多行

# 列表推导式完成上述任务
num_2 = [1, 2, 3, 4, 5]
num_2 = [i * 2 for i in num_2]
print(num_2)          # [2, 4, 6, 8, 10]
# 列表推导式很高效

# 列表推导式 and 循环体 之间的转化
x = [i for i in range(10)]
print(x)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = []
for i in range(10):
    x.append(i)
print(x)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 若是字符串呢？
y = [c * 2 for c in "FishC"]
print(y)              # ['FF', 'ii', 'ss', 'hh', 'CC']

# 若想要获得每个字符的编码呢？ord()
z = [ord(c) for c in "FishC"]   # ord(x)函数，是获取x的ASCII编码
print(z)              # [70, 105, 115, 104, 67]

# 在二维列表中，想要提取出来第二列的数据呢？
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
col2 = [row[1] for row in matrix]
print(col2)        # [2, 5, 8]

# 在二维列表中，获取主对角线上的元素
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
diag = [matrix[i][i] for i in range(len(matrix))]   # 可以使用索引值
print(diag)         # [1, 5, 9]

# 在二维列表中，获得反对角线上的元素
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
back_diag = [matrix[i][2 - i] for i in range(len(matrix))]
print(back_diag)    # [3, 5, 7]

"""
⚠ 列表推导式 和 循环体 是不一样的
循环体：逐个修改表内元素
列表推导式：直接创建一个新列表，然后赋值回列表变量名
"""