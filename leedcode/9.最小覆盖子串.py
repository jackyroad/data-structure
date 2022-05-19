# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hs, ht = defaultdict(int), defaultdict(int)
        i, j, cnt = 0, 0, 0
        ans = ""
        if len(s) < len(t):
            return ""
        for char in t:
            ht[char] += 1  # ht是字典哈希表
        while j < len(s):
            hs[s[j]] += 1
            # 先找出包含目标串的大的范围，在一步步从初始位置剔除多余的部分
            if hs[s[j]] <= ht[s[j]]:  # 这个保证了cnt不会超出s的长度
                cnt += 1  # cnt是计数目标字符串的个数，不会减小
            while hs[s[i]] > ht[s[i]] and i <= j:  # 通过这个循环，会剔除掉原串多余字符的部分
                hs[s[i]] -= 1
                i += 1
            if cnt == len(t):
                if not ans or len(ans) > j - i + 1:
                    ans = s[i:j + 1]
            j += 1
        return ans


a = Solution()
print(a.minWindow("ADOBECODEBANC", "ACB"))
