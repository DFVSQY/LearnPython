print("hello world!")

a, b = 20, 10
c = a + b
print(c)

# 字符串即可使用单引号也可使用双引号
message = "visual studio code"
print(message)
message = 'visual studio code'
print(message)
print(message.title())
print(message.upper())
print(message.lower())

# 字符串的format形式：f"{var}"
first_name = "bill"
last_name = "gates"
user_name = f"{first_name} {last_name}"
user_name_title = f"user_name:{user_name.title()}"
print(user_name_title)

# 移除字符串空白
user_name = " bill jobs "
print(user_name.lstrip())  # 移除开头空白
print(user_name.rstrip())  # 移除结尾空白
print(user_name.strip())  # 移除开头结尾空白

# 两个乘号表示乘方
print(3 ** 2)

# 浮点数运算结果的小数位数可能是不确定的
f = 0.2 + 0.1
print(f)  # 0.30000000000000004

# 除法运算中，结果总是浮点数
print(4 / 2)  # 2.0

# 其他运算中，如果一个操作数是整数，另一个是浮点数，结果也未浮点数
print(3 + 2.0)  # 5.0
print(3 * 2.0)  # 6.0
print(3.0 ** 2)  # 9.0

# 表示很大数时，可以用下划线分组便于阅读
universe_age = 14_000_000_000
print(universe_age)

# 通常用全大写表示该变量为常量
MATH_PI = 3.14
print(MATH_PI)