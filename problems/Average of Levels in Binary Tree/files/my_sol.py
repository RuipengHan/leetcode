# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = []
        queue = [root]
        while queue:
            nodes = queue.copy()
            queue.clear()
            sums = 0
            num = 0
            for node in nodes:
                # For each node in this layer, add its descendents
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sums += node.val
            avgs.append(sums / (1.0 * len(nodes)))
        return avgs



            