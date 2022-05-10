from Stack import Stack


# 括号匹配，遇到右括号前的最后一个左括号一定要与右括号匹配

def parChecker_v1(symbolString):
    s = Stack()
    index = 0
    balanced = True
    if len(symbolString) == 0:
        balanced = False
    while index < len(symbolString) and balanced:
        # while 是循环语句，if是条件判断语句，要注意两者区别
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False  # 这条语句意义:在())(这种情况下第一对括号已经匹配完了栈为空,先置错
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def parChecker_v2(symbolString):
    s = Stack()
    index = 0
    balanced = True
    if len(symbolString) == 0:
        balanced = False
    while index < len(symbolString) and balanced:
        # while 是循环语句，if是条件判断语句，要注意两者区别
        symbol = symbolString[index]
        if symbol in '{[(':  # 用in方法判断是否为左括号
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False  # 这条语句意义:在())(这种情况下第一对括号已经匹配完了栈为空,先置错
            else:
                pop = s.pop()
                if not match(pop, symbol):
                    balanced = False

        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def match(pop, symbol):
    right = "{[("
    left = "}])"
    return right.index(pop) == left.index(symbol)
    # index是字符串方法，检测字符串是否包含子字符串，返回子字符串出现的索引值


string1 = "())"
string2 = "{[]()"
print(string1, ":", parChecker_v1(string1))
print(string2, ":", parChecker_v2(string2))
