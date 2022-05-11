# 输入函数input,接受字符串作为参数，返回字符串
a_name = input("请输入任意字符：")
# print可以接受多个参数，用sep改变间隔，end改变结尾，通过%格式化字符串
a_name2 = (1, 2, 3)
print("你输入的是：", a_name, "输入的类型是：", type(a_name), sep="   ")
print("你输入的是：{} ".format(a_name))
# 元组类型数据输出
print("你输入的是：{2},{1},{0}".format(*a_name2))

# 对于赋值语句,赋值是·创造对象的引用而不是复制对象
a_list = [1, 2, 3, 4]
b_list = a_list
a_list.reverse()  # a_list=[4,3,2,1]
c_list = a_list
print(a_list, b_list, c_list)  # 输出都为[4,3,2,1]
