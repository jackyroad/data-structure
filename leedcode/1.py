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


test = Solution2()
print(test.isPalindrome(121))
