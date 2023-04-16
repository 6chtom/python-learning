"""
分支结构由if语句实现的
if 有五种语法结构，第5种为炫技不建议学，知道就好
"""

"""
1. 判断一个条件，如果这个条件成立，就执行其包含的某条语句或代码块

if condition:
    statement(s)

"""
if 3 < 5:
    print('3确实小于5')

#----------------------------------------------------------------------

"""
2. 判断一个条件，成立则执行某个语句或代码块，不成立则执行另一个语句或代码块

if condition:
    statement(s1)
else:
    statement(s2)

"""
if 3 == 5:
    print('3是5')
else:
    print('3不是5')

#----------------------------------------------------------------------

"""
3. 判断一个条件，成立则执行1，不成立则判断第二个条件，成立则执行2，不成立则判断第三个条件，类推

if condition1:
    statement(s1)
elif condition2:
    statement(s2)
elif condition3:
    statement(s3)
...

"""
score = input('请输入你的成绩：')
score = int(score)
if 0 <= score < 60:
    print('D')
elif 60 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
elif 90 <= score < 100:
    print('A')
elif score == 100:
    print('S')             # elif比全是if的效率快不少，因为全是if的话需要每次都判断，if-elif是一个完整的代码块，只要有判断成立的条件，那么直接跳出if-elif框架

#----------------------------------------------------------------------

"""
4. 在第3中后加一个else，用来决定判断条件都不成立时的输出
if condition1:
    statement(s1)
elif condition2:
    statement(s2)
elif condition3:
    statement(s3)
...
else:
    statement(x)

"""
score = input('请输入你的成绩：')
score = int(score)
if 0 <= score < 60:
    print('D')
elif 60 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
elif 90 <= score < 100:
    print('A')
elif score == 100:
    print('S')
else:
    print('请输入0~100之间的成绩')

#----------------------------------------------------------------------

"""
5. 炫技，和第2种一样

条件成立时执行的语句 if condition else 条件不成立时执行的语句

"""