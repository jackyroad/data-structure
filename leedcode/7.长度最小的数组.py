# 给定一个数组，求数组所有的子串中元素和比目标值小的子串长度
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口，用一个for循环遍历子数组，j指向子数组最后一个下标，i是子数组初始下标，不断逼近
        subLength = float('inf')
        sum = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                subLength = min(subLength, j - i + 1)
                # 因为无符合条件要返回0，所以可以把长度初始设置一个无穷大的数
                sum -= nums[i]
                i += 1
        return 0 if subLength == float('inf') else subLength
