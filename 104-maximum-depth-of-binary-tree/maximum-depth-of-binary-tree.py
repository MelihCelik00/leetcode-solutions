# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive depth-first search
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # worst case O(n)

        # Breadth First Search (Queue Implementation)
        # if not root:
        #     return 0

        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node=q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1

        # return level

        # Iterative Depth First Search (Stack Implementation)
        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.right, depth+1])
        #         stack.append([node.left, depth+1])
        
        # return res