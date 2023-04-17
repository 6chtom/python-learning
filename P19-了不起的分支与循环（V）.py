"""
for循环

for 变量 in 可迭代对象:
    statement(s)

可迭代对象: 元素可以被单独提取出来的对象, 比如字符串"FishC"
迭代: 从"FishC"当中依次取出 F i s h C 的过程称为迭代
"""
for each in "FishC":         # 给each赋值"FishC"中的每一个字符，并打印出来
    print(each)

# 用while也可以做到FishC的遍历
i = 0
while i < len("FishC"):          # len()是得到当前字符串的长度length，len("FishC")的输出结果是5
    print("FishC"[i])            # 中括号为下表索引，也就是依次索引字符串的字符，起始字符为0
    i += 1

j = 0
sum = 0
for j in range(1,1000001):       # range()经常和for循环一起使用，range就是帮助生成一个可迭代的数字序列
    sum += j                     # 用法：range(stop)、range(start,stop)、range(start,stop,step)
    j += 1                       
print(sum)

for a in range(2,10):            # range(start,stop)中包含start，但不包含stop（前包含后不包含）
    print(a)                     # 打印出来是23456789

for b in range(4, 10, 2):
    print(b)                     # 打印出来是468，意思是包含start，然后start+2

for c in range(10, 4, -2):       # step还支持负数，这样就是减了
    print(c)                     # 打印结果是10 8 6

"""
for 循环的嵌套
"""
# 找到10以内的素数，素数：除了1和其本身，无法被其他数整除的数
for n in range(2, 10):                   # 因为素数只能是从2开始，所以直接以2为起始
    for x in range(2, n):                # 除数同样以2开始
        if n % x == 0:                   # n可以被x整除
            print(f"{n}={x}×{n // x}")   # 把n和x的关系写出来
            break                        # 既然已经判定n不是素数，那么直接跳出第二层for循环
    else:                                # n不能被任何一个2到9的数字整除，所以n是素数
        print(f"{n}是一个素数")

print('test')