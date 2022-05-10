class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):  # 判断栈空
        return self.item == []

    def push(self, item):  # 将一个元素推入栈中
        self.item.append(item)

    def pop(self):  # 将栈顶元素出栈
        return self.item.pop()

    def peak(self):  # 返回栈顶元素，对栈不做修改
        return self.item[len(self.item) - 1]

    def size(self):  # 返回栈长
        return len(self.item)


if __name__ == '__main__':
    s = Stack()

    print(s.isEmpty())
    s.push("abc")
    s.push({1, 2, 3})
    s.push(("a", "b"))
    print(s.pop(), s.pop())
    print(s.peak())
    print(s.size())
