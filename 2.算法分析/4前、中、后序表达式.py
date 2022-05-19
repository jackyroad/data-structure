from Stack import Stack
import string


# 前序和后序表达式中操作数不受影响，所以建立一个栈存放运算符，一个列表放操作数
# 中序转后序
def infixToPostfix(infix):
    pre = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opstack = Stack()
    postifxlist = []
    tokenList = infix.split()
    for token in tokenList:
        if token in string.ascii_uppercase:
            postifxlist.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            topToken = opstack.pop()
            while topToken != "(":
                postifxlist.append(topToken)
                topToken = opstack.pop()
        else:
            while not opstack.isEmpty() and pre[opstack.peak()] >= pre[token]:
                postifxlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postifxlist.append(opstack.pop())
    return " ".join(postifxlist)


def postfixEval(postfix):
    opstack = Stack()
    tokenList = postfix.split()
    for token in tokenList:
        if token in string.digits:  # 检测字符串是否为0~9的数字
            opstack.push(int(token))
        else:
            try:
                operand1 = opstack.pop()
                operand2 = opstack.pop()
            except:
                print("表达式错误！")
                return False
            result = domath(operand1, operand2, token)
            opstack.push(result)
    return opstack.pop()


def domath(op1, op2, token):
    if token == "*":
        return op2 * op1
    elif token == "/":
        return op2 / op1
    elif token == "+":
        return op2 + op1
    elif token == "-":
        return op2 - op1


# print(infixToPostfix("( A + B ) * C"))
print(postfixEval("1 5 5 + * "))
