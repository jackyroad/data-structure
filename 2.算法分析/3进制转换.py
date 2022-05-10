from Stack import Stack


# 0~9进制转换
def divideBy2(number, base):
    s = Stack()
    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base

    binString = ""
    while not s.isEmpty():
        binString += str(s.pop())

    return binString


# 16以内进制转换
def divideBy16(number, base=16):
    s = Stack()
    digits = "0123456789ABCDEF"
    while number > 0:
        rem = number % base
        s.push(rem)
        number = number // base

    binString = ""
    while not s.isEmpty():
        binString += str(digits[s.pop()])

    return binString


dc_number = 17
print(dc_number, divideBy2(dc_number, 2))
print(dc_number, divideBy16(dc_number, 16))
