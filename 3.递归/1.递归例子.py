# 递归三要素：递归算法有基本情况；要把所求问题向基本情况靠拢；递归函数递归的调用自己
def sum_list(List):
    if len(List) == 1:
        return List[0]
    else:
        return List[0] + sum_list(List[1:])


a = [1, 2, 3, 4, 5]
print(sum_list(a))
print(7//2)
