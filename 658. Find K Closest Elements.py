'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''


class Solution:
    def findClosestElements(self, arr, k: int, x: int):

        def binarySearch(arr, target, k):
            ans = []
            left, right = 0, len(arr) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if target <= arr[mid]:
                    right = mid
                else:
                    left = mid

            # if arr[left] == target: return left
            # if arr[right] == target: return right

            while k and (right < len(arr) or left >= 0):
                if right < len(arr) and left >= 0:
                    if abs(arr[left] - target) <= abs(arr[right] - target):
                        ans.insert(0, arr[left])
                        left -= 1
                    else:
                        ans.append(arr[right])
                        right += 1
                elif left >= 0:
                    ans.insert(0, arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1

                k -= 1

            return ans

        return binarySearch(arr, x, k)
