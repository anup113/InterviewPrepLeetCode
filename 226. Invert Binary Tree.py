'''
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if not node:
                break
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
