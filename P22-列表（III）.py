"""
改：      就是赋值
1. 赋值： 替换某个元素
2. 切片： 替换某个切片内的元素
3. 排序： sort(Key=None, reverse=False), reverse()
"""

# 赋值
heros = ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
heros[4] = "无限宝石"     # 给第五个元素赋值 "无限宝石"
print(heros)             # ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '无限宝石', '雷神']

# 切片
heros = ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
heros[3:5] = ['武松','林冲','李逵']     # 第3个元素之后到第5个元素赋值这三个字符串，无论原来的元素有几个
print(heros)                           # ['钢铁侠', '绿巨人', '黑寡妇', '武松', '林冲', '李逵', '雷神']

# 从小到大排序   sort()函数直接排序
numbers = [3,1,9,2,4,5,7,8]
numbers.sort()
print(numbers)           # [1, 2, 3, 4, 5, 7, 8, 9]

# 从大到小排序   先用sort()进行从小到大排序，再用reverse()进行倒转
numbers = [3,1,9,2,4,5,7,8]
numbers.sort()
numbers.reverse()        # reverse()仅仅是倒转
print(numbers)           # [9, 8, 7, 5, 4, 3, 2, 1]

# 直接从大到小排序，sort(Key = None, reverse = False)
# 有两个参数，Key指的是可以使用指定算法进行排序，现在可以忽略
# reverse可以直接填True或False
numbers = [3,1,9,2,4,5,7,8]
numbers.sort(reverse = True)
print(numbers)           # 可以直接得到[9, 8, 7, 5, 4, 3, 2, 1]

#-------------------------------------------------------#

"""
查： 查询任何列表内容
1. count(): 查询列表中有多少个相同元素
2. index(x,start,end): 查询某个元素的索引值，即下标
3. copy()： 拷贝一个列表，但这是“浅拷贝”
"""
# count()
numbers = [3,1,3,2,3,5,3,3]
print(numbers.count(3))   # 5

# index()
heros = ['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
print(heros.index("绿巨人"))     # 1     但是注意index()只能索引第一个出现的该值
# 想要替换某个确定的值
heros[heros.index("绿巨人")] = "神奇女侠"
print(heros)                     # ['钢铁侠', '神奇女侠', '黑寡妇', '鹰眼', '灭霸', '雷神']

# index(x,start,end)，指定范围查找某个值
numbers = [3,1,3,2,3,5,3,3]
print(numbers.index(3, 3, 5))    # 4

# copy()
nums_copy1 = numbers.copy()
print(nums_copy1)            # [3, 1, 3, 2, 3, 5, 3, 3]
# 或
nums_copy2 = numbers[:]
print(nums_copy2)            # [3, 1, 3, 2, 3, 5, 3, 3]

