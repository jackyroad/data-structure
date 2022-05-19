import collections


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        i = 0
        ans = 0
        count = collections.Counter()  # 返回一个字典
        for j, elm in enumerate(fruits):  # j是下标，elm是元素
            count[elm] += 1  # 字典的键值对，对元素分类如{1:2,0:1，2:1}
            while len(count) >= 3:
                count[fruits[i]] -= 1  # 因为多余的元素可能不止一个，反应在字典就是值大于1，所以需要一直减到0为止
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            ans = max(ans, j - i + 1)

        return ans


a = Solution()
print(a.totalFruit([1, 1, 0, 2]))
