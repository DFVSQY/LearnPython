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

# 打印数组会将方括号一起打印出来
titles = ["file", "edit", "selection", "view", "go", "run", "terminal", "help"]
print(titles)

# 打印列表元素
print(titles[0])  # 首个元素
print(titles[-1])  # 最后一个元素
print(f"the first title is:{titles[0]}")

# 修改列表元素值
titles[0] = "File"
print(titles)

# 列表末尾添加元素
titles.append("Debug")
print(titles)

# 在指定位置插入元素
titles.insert(2, "Edit")
print(titles)

# # python并未限制列表元素为同一类型，但最好不要这么干
# titles.insert(0, 0)
# titles.append(-1)
# print(titles)

# 使用del方法删除列表元素
del titles[3]
del titles[-2]
print(titles)

# 使用pop方式删除列表指定位置的值
d1 = titles.pop()  # 删除列表末尾元素的值，并返回删除的值
d2 = titles.pop(0)  # 删除列表指定位置的值并返回删除的值，此处为第一个元素
print(d1, d2)
print(titles)

# # 删除列表中指定的值
# titles.remove("File")
# print(titles)

# 对列表进行排序
titles.sort()
print(titles)
titles.sort(reverse=True)
print(titles)

# 对列表进行排序，但不改变原来列表的内容
print(sorted(titles))
print(titles)
print(sorted(titles, reverse=True))
print(titles)

# 将列表倒转
titles.reverse()
print(titles)

# 输出列表长度
print(len(titles))

# 遍历列表
for title in titles:			# for语句后每个缩进都是循环的一部分(python通过缩进判断代码行之间的关系)
	print(title)
	print(title.title())
	print(title.upper())

print("traverse list finish!")
