'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        def getStartingPos(arr, target):
            left, right = 0, len(arr)-1
            while left + 1 < right:
                mid = (left + right) // 2

                if target <= arr[mid]:
                    right = mid

                else:
                    left = mid

            if arr[left] == target:
                return left
            if arr[right] == target:
                return right

            return -1

        def getEndingPos(arr, target):
            left, right = 0, len(arr)-1
            while left + 1 < right:
                mid = (left + right) // 2

                if target >= arr[mid]:
                    left = mid

                else:
                    right = mid

            if arr[right] == target:
                return right
            if arr[left] == target:
                return left

            return -1

        start = getStartingPos(nums, target)
        end = getEndingPos(nums, target)

        return [start, end]
