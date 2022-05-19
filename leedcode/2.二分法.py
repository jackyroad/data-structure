# 二分法从列表中找出对应数的下标，没有返回-1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a, b = 0, len(nums) - 1
        while a <= b:
            mid = (b - a) // 2 + a
            if target > nums[mid]:
                a = mid + 1
            else:
                if target == nums[mid]:
                    return mid
                else:
                    b = mid - 1

        return -1
