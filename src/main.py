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
