"""
布尔类型只有两种: True or False
大部分情况下布尔类型为True
定义为False的情况一般如下:
1. 定义为False的对象: None 和 False
2. 值为0的数字类型: 0, 0.0, 0j, Decimal(0), Fraction(0,1)
3. 空的序列和集合: '', (), [], {}, set(), range(0)
"""

# 直接使用布尔类型函数 bool(x) 可以直接知道真假
print(bool(500)) # true
print(bool('假')) # true
print(bool('False')) # true
print(bool(False)) # false
print(bool('')) # false
print(bool(' ')) # true
print(bool(0)) # false
print(bool(0.0)) # false
print(bool(0j)) # false

# 布尔类型其实就是特殊的整型，True == 1， False == 0
print(True + False)  # 结果为1

"""
逻辑运算符（三个）: and / or / not   与门，或门，非门
and: 左边和右边同时为True, 结果为True
or: 左边和右边有一个为True, 结果为True
not: 得到与操作数相反的布尔类型值
"""

print(3 < 4 and 4 < 5)  # True
print(3 > 4 or 4 > 5)  # False
print(not True)  # False
print(not 0)  # True

# 如果不是运算结果而是数字或者字符串进行与或非呢？
"""
and中, 同真出后者, 有假出假者, 同假出前者
or中, 同假出后者, 有真出真者, 同真出前者
"""
print(3 and 4)  # 4
print(4 and 5)  # 5
print('FishC' and 'Love')  # Love
print(3 or 4)  # 3
print(4 or 5)  # 4
print("FishC" or "Love")  # FishC
print(0 and 5) # 0
print(0j and 0j) # 0j