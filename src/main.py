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

# range(1, 5)生成一系列数(此时range的结果不是数字列表)，输出：
# 1
# 2
# 3
# 4
for value in range(1, 5):
    print(value)

# 创建数字列表
numbers = list(range(1, 5))
print(numbers)		# [1, 2, 3, 4]

# range可通过第三个参数指定步长
odd_numbers = list(range(1, 5, 2))
print(odd_numbers)  # [1, 3]

# range也支持指定负数步长
odd_numbers = list(range(5, 0, -2))
print(odd_numbers)  # [5, 3, 1]

# 对数字列表进行简单的统计计算
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
print(min(squares), max(squares), sum(squares))  # 对数字列表进行一些简单的统计计算

# 列表解析
squares = [value ** 2 for value in range(1, 11)]  # 列表名 = [元素生成表达式 for循环]
print(squares)

titles = ["file", "edit", "selection", "view", "go", "run", "terminal", "help"]

title1, title2, title3 = titles[0:3]
print(title1, title2, title3)  # file edit selection
print(titles[1:3])  # ['edit', 'selection']
print(titles[:3])  # ['file', 'edit', 'selection']
print(titles[3:])  # ['view', 'go', 'run', 'terminal', 'help']
print(titles[-3:])  # ['run', 'terminal', 'help']

# copy list
# 输出：['file', 'edit', 'selection', 'view', 'go', 'run', 'terminal', 'help']
print(titles[:])

# 起始值的索引不能比终止值更靠前
print(titles[3:1])  # []
t = titles[3:1]
print(t)  # []

# 遍历列表切片
for title in titles[1:3]:
    print(title)

# 元组：python中不可修改的列表，使用逗号分割表示，可选用小括号括起来（只是为了方便看起来更整洁）
fix_titles = "file", "edit", "selection", "view", "go", "run", "terminal", "help"

# 输出：('file', 'edit', 'selection', 'view', 'go', 'run', 'terminal', 'help')
print(fix_titles)

fix_titles = ("file", "edit", "selection", "view",
              "go", "run", "terminal", "help")

# 输出：('file', 'edit', 'selection', 'view', 'go', 'run', 'terminal', 'help')
print(fix_titles)

# 由于元组是由逗号定义的，所以只有一个元素的元组第一个元素后必须加上逗号
only_one_tuple = ("OnlyOne",)
print(only_one_tuple)

# 这种形式只是一个字符串
only_one_str = ("OnlyOne")
print(only_one_str)  # OnlyOne

# 虽然不可修改元组内容，但可以修改变量的元组引用
fix_titles = ("File", "Edit", "Selection")
print(fix_titles)  # ('File', 'Edit', 'Selection')

"""
if 语句文档的补充：https://docs.python.org/3/library/stdtypes.html#truth-value-testing

Truth Value Testing:

Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero, when called with the object. 1 Here are most of the built-in objects considered false:

constants defined to be false: None and False.

zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)
"""

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car != "bmw":
        print(car.title())
    else:
        print(car.upper())

nums = [10, 30, 20, 5, 1, 3]
for num in nums:
    if num >= 20:
        print(num, ">= 20")
    elif num > 10:
        print(num, "> 10")
    else:
        print(num, "<= 10")

for num in nums:
    if num <= 20 and num >= 10:
        print(num, "<= 20 and >= 10")
    elif num > 20 or num <= 5:
        print(num, "> 20 or <= 5")

num = 20
if num in nums:
    print("num 20 in nums")

num = 25
if num not in nums:
    print("num 25 not in nums")

if nums:  # 在if 语句中将列表名用作条件表达式时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False
    print("nums is not empty")

empty_nums = []
if not empty_nums:
    print("empty_num is empty")

# 字典用放在花括号{}中的一系列键值对表示
# 键和值之间用冒号分隔，而键值对之间用逗号分隔
titles = {"file": "File", "edit": "Edit", "selection": "Selection"}

# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键
print(titles["file"])  # 使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：如果指定的键不存在就会出错
print(titles["selection"])
print(titles)

# 为字典添加键值对
titles["view"] = "View"
titles["go"] = "Go"
print(titles)

# 修改字典中的值
titles["file"] = "File Save"
print(titles)

# 删除字典中的键值对
del (titles["file"])  # 只能删除存在的key，删除不存在的key会报错
print(titles)

# 如果指定的键有可能不存在，应考虑使用方法get() ，而不要使用方括号表示法
# 方法get() 的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选的
print(titles.get("file"))  # output: None

#output: dict_items([('edit', 'Edit'), ('selection', 'Selection'), ('view', 'View'), ('Go', 'Go')])
print(titles.items())  # items方法返回一个键值对列表

# 遍历字典
for key, value in titles.items():
    print(key, value)

# 遍历字典中的所有key
for key in titles.keys():
    print(key)

# 遍历字典中的所有value
for value in titles.values():
    print(value)

# 从Python 3.7起，遍历字典时将按插入的顺序返回其中的元素。
# 不过在有些情况下，你可能要按与此不同的顺序遍历字典。
# 要以特定顺序返回元素，一种办法是在for 循环中对返回的键进行排序。
# 为此，可使用函数sorted() 来获得按特定顺序排列的键列表的副本
for key in sorted(titles.keys()):
    print(key)

titles["File"] = "File"
titles["Go"] = "Go"
print(titles)

# 为剔除重复项，可使用集合set
# 集合中的每个元素都必须是独一无二的
for value in set(titles.values()):
    print(value)

person_1 = {"name": "Bill", "age": 18, "sex": "man"}
person_2 = {"name": "Job", "age": 23, "sex": "women"}
persons = [person_1, person_2]
print(persons)

editor = {
    "menus": ["file", "edit", "selection", "view", "go"],
    "name": "visual studio code",
}
print(editor)

users = {
    "Bill": {
        "Name": "Bill Gates",
        "Sex": "Man",
        "Age": 50,
    },
    "Jobs": {
        "Name": "Steve Jobs",
        "Sex": "Man",
        "Age": 40,
    },
}
print(users)

open_test_input = False
if open_test_input:
    # 使用函数input()时，Python将用户输入解读为字符串
    message = input("Tell me something, I will repeat it back to you:")
    print(message)

    age = input("how old are you? ")
    age = int(age)  # 将字符串转换为整数
    print(age)

# 求模运算
print(22 % 5)  # output: 2

# while 示例
cur_num = 0
while cur_num <= 5:
    print(cur_num)
    cur_num = cur_num + 1

# break 示例
cur_num = 0
while True:
    print(cur_num)
    cur_num = cur_num + 1
    if cur_num > 5:
        break

# continue 示例
cur_num = 0
while cur_num <= 10:
    old_num = cur_num
    cur_num = cur_num + 1
    if old_num % 2 != 0:
        continue
    print(old_num)

# while结合列表：列表间移动元素
unconfirm_users = ["alice", "bill", "jobs"]
confirm_users = []
while unconfirm_users:
    user = unconfirm_users.pop()
    print(f"valid user:{user}")
    confirm_users.append(user)

# while结合列表，移除列表的特定元素
animals = ["cat", "dog", "cat", "fish", "cat", "rabbit"]
while "cat" in animals:
    animals.remove("cat")
print(animals)

# 后面的所有缩进行构成了函数体


def hello_world():
    """
    此处的文本是称为文档字符串 （docstring）的注释，描述了函数是做什么的。
    文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。

    显示简单的问候语
    """
    print("hello world")


hello_world()


def greet_user(username):
    print(f"Hello, {username.title()}!")


greet_user("Bill")


def des_pet(animal_type, animal_name):
    print(f"I have a {animal_type}, its name is {animal_name}")


# 调用函数时，可使用位置实参，这要求实参的顺序与形参的顺序相同
des_pet("dog", "harry")

# 调用函数时，也可使用关键字实参 ，其中每个实参都由变量名和值组成，关键字实参的顺序无关紧要
des_pet(animal_name="harry", animal_type="dog")


def des_editor(user_name, editor_name="vscode"):
    """ 默认参数, 带默认值的参数需要放到最后面 """
    print(f"{user_name} favaritor editor is: {editor_name.title()}")


# 默认参数的使用
des_editor("Bill")
des_editor("Jobs", "sublime text")
des_editor(editor_name="notepad", user_name="Jim")


def format_name(first_name, last_name, middle_name=""):
    if not middle_name:  # Empty or Null
        full_name = f"{first_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    return full_name


# 带返回值函数
print(format_name("bill", "gates"))
print(format_name("steve", "jobs", "jim"))


def build_person(first_name, last_name, age=None):
    person = {"first_name": first_name.title(), "last_name": last_name.title()}
    if age:  # not (None or 0)
        person["age"] = age
    return person


#output: {'first_name': 'Steven', 'last_name': 'Jobs', 'age': 20}
print(build_person("steven", "jobs", 20))

#output: {'first_name': 'Bill', 'last_name': 'Gates'}
print(build_person("bill", "gates", 0))


def title_modify(titles):
    """ 修改列表 """
    if not titles:
        return
    num = len(titles)
    for i in range(num):
        titles[i] = titles[i].title()


menus = ["file", "edit", "selection", "view", "go", "run", "terminal", "help"]
title_modify(menus[:])  # 传递是menus副本，不会修改menus本身
print(menus)

title_modify(menus)  # 会修改menus本身
print(menus)


def build_profile(first_name, last_name, **user_info):
    """
    使用任意数量的关键字实参

    形参**user_info 中的两个星号让
    Python创建一个名为user_info 的空字典，并将收到的所有名称值
    对都放到这个字典中
    """
    user_info['first_name'] = first_name
    user_info['last name'] = last_name
    return user_info


user_profile = build_profile(
    "Bill", "Gates", location="China", age=18, sex="Man")
print(user_profile)
