# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both are empty
            return True
        if not p or not q: # one if is them empty
            return False
        if p.val != q.val: # node value mismatch
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) # both must be True for outcome to be True 