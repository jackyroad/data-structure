# 1 Python内建原子数据类型
# Python有两大内建数据类实现整数型与浮点型，标准数学运算符：+ - * / **（幂），其他包括取余（取模）%、取整//
print(7 // 3)
print(7 % 3)
# Python通过布尔类实现布尔数据类型，布尔运算符有and or not
print(True and False)
print(True or False)
print(not (True or False))
# 2 内建集合数据类型
# 列表、字符串和元组是有序集合，集和字典是无序集合。
# 数据类型：整数 Int、浮点数 Float、布尔值 Bool、字符串 Str、列表 List、元组 Tuple、字典 Dict、集合 Set，也就是说集合内的元素只能是这些。

# 2.1 列表是[x,x,x],列表运算包括[](索引),+(连接),*(重复),[:](切片),in(成员),len(长度)
# 列表的方法包括append、insert、pop、reverse、sort、del、index、count、remove
# range函数会生成一个代表值序列的范围对象，通过list函数将范围对象的值以列表形式表现出来
print((range(0, 10)), list(range(0, 10)))


# 2.2 字符串是字母、数字和其他符号的有序集合“xxx”或‘xxx’，除了序列运算符外，还有一些特有方法，包括center、count、ljust，rjust，lower、upper
# find、split
# 列表可以修改，但是字符串不可修改
# split为字符串方法，指定分割符对字符串切片，默认为空格、\n,\t。返回一个字符串列表。
a = 'axbj 125A'
print(a.split())


# 2.3 元组与列表类似(x,x,x)，但是不可修改


# 2.4 集是无序集合{x，x，x}，集内不允许重复元素，集的运算符号包括|,&,<=,-,in,len,集、字典内元素不能为集，列表,字典(不可哈希）
# {[[x,x],[x,x]]}可迭代，但{[x,x],[x,x]}不可迭代。集的方法包括union(和)、intersection(共有)、difference(特有)、
# issubset(子集)、add、pop、remove、clear
set1 = {1, "cd", (1, "a"), 8, 9}
set2 = {1, "cd", (1, "a")}
print(set1 <= set2)
print(set1.pop())


# 2.5 字典是键—值对的形式,dict对键有哈希要求，对值没有限制。运算符包括[]、in、del,方法包括keys、value、items、get
dict1 = {(2, 3): [4, 5]}
print(dict1, dict1[(2, 3)], dict1.get(2, "no find"))
