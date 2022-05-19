#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = []  # 所有层的数字
        for i in range(numRows):
            row = []  # row是i层的数字
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(dp[i - 1][j - 1] + dp[i - 1][j])
            dp.append(row)
        return dp
