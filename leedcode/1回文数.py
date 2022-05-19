# 1.回文数
# 时间2022/5/11
class Solution1(object):
    def isPalindrome(self, x):  # 输入-121
        """
        :type x: int
        :rtype: bool
        """
        a = []
        b = str(x)
        c = True
        d = []
        e = []
        for i in range(len(b)):
            a.append(b[i])  # a应该为-121
        d += a
        a.reverse()
        e += a
        for i in range(len(a)):
            if e[i] != d[i]:
                c = False

        return c


# 简单实现，将输入转换为字符串后，用字符串的切片操作反序
class Solution2(object):
    def isPalindrome(self, x):  # 输入-121
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


# 为了减少内存空间，加快运行时间，可以考虑反转一半的数字
class Solution3(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):  # 数字为负，或最后一位为负0且原数字不为0则返回错
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x//10

        return revertedNumber == x or x == revertedNumber // 10  # 当为数字数位为奇数时，中间位不影响，直接省去


test = Solution3()
print(test.isPalindrome(-121))
