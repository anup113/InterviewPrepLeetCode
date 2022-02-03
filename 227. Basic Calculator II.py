'''
227. Basic Calculator II
Medium

3881

516

Add to List

Share
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
'''


class Solution:
    def calculate(self, s: str) -> int:
        '''
        1 <= len(s) <= in memmory
        s - + - * /
        is the expressio valid 
        take care of division by zero 
        undefined value 0/0


        13 + 2 * or / 2 -> 3 + 4 = 7

        3 + 2 + or - 2 -> 7

        stack [3, 2, -2] if next == * pop
                    else we will add
        '''
        stack = []
        operator = '+'
        s = s.replace(' ', '')
        operators = ['+', '-', '*', '/']
        n = len(s)
        prev = 0

        for i in range(n):
            char = s[i]

            if char.isdigit():
                number = prev * 10 + int(char)

            if not char.isdigit() or i == n-1:
                if operator == '+':
                    stack.append(number)
                if operator == '-':
                    stack.append(-number)
                if operator == '*':
                    stack.append(stack.pop() * number)
                if operator == '/':
                    temp = stack.pop()
                    if temp < 0:
                        value = -1 * (abs(temp) // number)
                    else:
                        value = temp // number
                    stack.append(value)
                operator = char
                number = 0
                # print(stack)

            prev = number

        print(stack)
        return sum(stack)
