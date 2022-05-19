# 给你一个按非递减顺序 排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums


class Solution2(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]5
        :rtype: List[int]
        """
        # 双指针，i,j指向头和尾，k用于新数组的下标。头和尾的元素平方那个大就进入新数组，当i=j时全部元素进入了新数组
        i, j, k = 0, len(nums) - 1, len(nums) - 1
        ans = [0] * (j+1)

        while i <= j:
            if nums[i] ** 2 > nums[j] ** 2:
                ans[k] = nums[i] ** 2
                i += 1
            else:
                ans[k] = nums[j] ** 2
                j -= 1
            k -= 1
        return ans


a = Solution2()
print(a.sortedSquares([-4, 1, 2, 3]))
