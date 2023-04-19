# 地板除"//"，其实就是向下取整
print(3 // 2)  # 输出 1
print(-3 // 2)  # 输出 -2

# 求余 "%"
print(3 % 2)  # 打印 1
print(6 % 2)  # 打印 0

###  所以有一条公式   x == (x // y) * y + (x % y)
###  有一个函数专门求这两个部分， divmod(x, y)，作用是返回(x//y,x%y)
print(divmod(3,2))  # 打印出来(1,1)
print(divmod(-3,2))  # (-2, 1)

# 绝对值函数 abs(x)
print(abs(-3.14))   # 3.14
print(abs(1+2j))  # 得到的是复数的模

# int(x) 得到x转换的整数
print(int('520'))
print(int(-3.94))  # 得到的是截掉小数点后面的整数 -3

# float(x) 得到x转换的浮点数
print(float('3.14'))  # 3.14
print(float(314))  # 314.0
print(float('+1e6'))  # 也可以转换E记法为浮点数

# complex(x) 得到x转换的复数
print(complex('1+2j')) # (1+2j)，中间的复数字符串不能有空格

# pow(x,y) 计算x的y次方，或者可以直接用x**y，也可以得到同样的结果
print(pow(2,3))  # 8
print(2 ** 3)  # 8
print(pow(2, -3)) # 0.125
# pow(x,y,z) 还可以添加一个z参数，表示x**y后%z求余
print(pow(2,3,5))  # 3 
