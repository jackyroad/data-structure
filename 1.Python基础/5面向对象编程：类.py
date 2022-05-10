# 1 Fraction是构造的方法，self是指向对象的形式参数，my_fraction是建立的实例对象
def gcd(m, n):  # 实现求最大公约数
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, top=3, bottom=5):  # init不要写成int
        self.num = top
        self.den = bottom

    # 打印实例对象本身会指向它的实际地址，通过__str__方法可以打印对象中的具体属性
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print("{}/{}".format(self.num, self.den))

    # 通过__add__方法实现对象的相加
    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        common = gcd(num, den)
        return Fraction(num // common, den // common)

    # 有两个实例只有当他们是同一对象的引用时才相等，这是浅相等，通过__eq__重写
    def __eq__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return num == den


my_fraction = Fraction(3, 6)
my_fraction2 = Fraction(3, 4)
my_fraction3 = Fraction(3, 5)
print(my_fraction)
print(my_fraction.show())
print(my_fraction + my_fraction2)
print(my_fraction == my_fraction3)


# super函数会查找方法的超类，超类的超类，直到找到所有特性
class A:
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


d = D()


# 2 类的继承：逻辑门与电路逻辑(与门非门或门)
# 类LogicGate代表逻辑门的通用特性：逻辑运算的标签和一个输出，这是所有逻辑门的超类
class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None  # None表示空，单不等于空字符串、空列表、False

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.PerformGatelogic()
        # 创建了方法，但实际代码不存在。self指向实际调用对象的引用，任何新添加的逻辑门只需实现PerformGatelogic()
        return self.output


# 通过逻辑门的输入个数分为2类，与门与或门一类(2),非门一类(1)
class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getpinA(self):
        if self.pinA is None:
            return int(input("Enter pinA  for gate" + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getpinB(self):
        if self.pinB is None:
            return int(input("Enter pinB  for gate" + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error:no empty pin")


class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None

    def getpinA(self):
        if self.pinA is None:
            return int(input("Enter pin  for gate" + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            raise RuntimeError("Error:no empty pin")


class Connector:
    def __init__(self, f_gate, t_gate):  # 建立两个实例对象
        self.f_gate = f_gate
        self.t_gate = t_gate
        t_gate.setNextPin(self)  # 连接器对象的下一个逻辑门的流入

    def getFrom(self):
        return self.f_gate

    def getTo(self):
        return self.t_gate


# BinaryGate类和UnaryGate类的目的是添加输入，具体逻辑门的实现以之为父类，继承输入、输出、标签，不需要添加新的数据
class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def PerformGatelogic(self):
        a = self.getpinA()
        b = self.getpinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def PerformGatelogic(self):
        a = self.getpinA()
        b = self.getpinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def PerformGatelogic(self):
        a = self.getpinA()
        if a == 1:
            return 0
        else:
            return 1


if __name__ == '__main__':
    g1 = AndGate("与门")
    g2 = AndGate("与门")
    g3 = OrGate("或门")
    g4 = NotGate("非门")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())
