# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # beats 100%(runtime)
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        max_cnt = 1
        stack = [(root, 1)]
        while stack:
            
            cur_node, cur_cnt = stack.pop()
            max_cnt = max(max_cnt, cur_cnt)

            if cur_node.left: stack.append((cur_node.left, cur_cnt+1))
            if cur_node.right: stack.append((cur_node.right, cur_cnt+1))

