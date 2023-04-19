"""
分支结构的嵌套，if中嵌套if
"""

age = 18
isMale = True
if age < 18:
    print('抱歉，未满18岁')
else:
    if isMale != True:
        print('抱歉，仅限男性')
    else:
        print('欢迎')
