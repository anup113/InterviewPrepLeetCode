'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0
        res = []

        while n1 >= 0 or n2 >= 0:
            x1 = ord(num1[n1]) - ord('0') if n1 >= 0 else 0
            x2 = ord(num2[n2]) - ord('0') if n2 >= 0 else 0
            val = str((x1 + x2 + carry) % 10)
            carry = (x1 + x2 + carry) // 10
            res.append(val)
            n1 -= 1
            n2 -= 1

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])
