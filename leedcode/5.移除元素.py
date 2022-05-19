# python 中没有内置数组，用列表代替。数组是存放在连续内存空间上相同类型数据的集合
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 双指针法，快指针用于遍历数组，慢指针用于指向新数组
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex


a = Solution()
print(a.removeElement([1, 2, 2, 3, 4], 4))
