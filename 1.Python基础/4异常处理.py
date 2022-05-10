# 程序遇到的异常错误包括语法错误和逻辑错误，遇到逻辑错误可以用try-except语句处理；也可以用raise抛出异常
import math

a = -2
try:
    print(math.sqrt(a))
except:
    print("请输入非负数。")

if a < 0:
    raise RuntimeError("请输入非负数")

