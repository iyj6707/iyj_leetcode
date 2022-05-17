# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check_same(self, cur, target):
        if cur.val != target.val:
            return False
        if cur.left and target.left:
            self.check_same(cur.left, target.left)
        if cur.right and target.right:
            self.check_same(cur.right, target.right)
        return True
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque([cloned])
        while queue:
            cur = queue.popleft()
            if cur.val == target.val and self.check_same(cur, target):
                return cur
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    
    