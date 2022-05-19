# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# dp(i)表示有多少种方法可以爬上i层，可以从n-1层或n-2层爬上n层,转化为斐波那契数列dp(n)=dp(n-1)+dp(n-2)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(0, n+1):
            # range()是默认从0开始的右开区间，所以这里i的含义是确定dp[i]的爬楼方法
            for j in range(1, 3):
                # j是可以爬楼的步数，3代表可以1步或是2步
                if i - j >= 0:
                    dp[i] += dp[i - j]

        return dp[n]


a = Solution2()
print(a.climbStairs(6))
