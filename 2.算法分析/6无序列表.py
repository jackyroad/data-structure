class Node:
    def __init__(self, initdata):
        # 节点是构建列表的基本结构，包含数据信息和指向下一个节点的应用
        self.data = initdata
        self.next = Node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext
