# Python 计算会产生一定的误差，浮点数计算要小心
x = 0.1+0.2
print(x)  # 计算结果是 0.30000000000000004


# 要想解决上述问题需要 decimal 模块
import decimal
a = decimal.Decimal('0.1') # 这是字符串
b = decimal.Decimal('0.2')
print(a + b)   # 打印出 0.3 很精确

# 科学计数法
print(0.00005)   # 打印出来是 5e-05，（5×10^(-5)）

# 复数，包含实部+虚部
i = 1 + 2j  # 复数赋值
d = i.real  # 复数实部
v = i.imag  # 复数虚部
print("实部为",d,"虚部为",v)  # 实部为 1.0 虚部为 2.0
