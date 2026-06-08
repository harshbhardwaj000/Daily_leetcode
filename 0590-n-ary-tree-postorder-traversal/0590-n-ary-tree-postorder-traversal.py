"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        if root is None:
            return []
        
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in node.children:
                stack.append(child)
        return result[::-1]