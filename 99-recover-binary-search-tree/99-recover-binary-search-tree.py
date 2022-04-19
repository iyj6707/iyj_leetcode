# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        
        def append_fn(seq, node):
            seq.append(node.val)
            
        def pop_fn(seq, node):
            node.val = seq.pop(0)
        
        def in_order_traversal(root, fn):
            if not root:
                return root
            in_order_traversal(root.left, fn)
            fn(nodes, root)
            in_order_traversal(root.right, fn)
            
        in_order_traversal(root, append_fn)
        nodes.sort()
        in_order_traversal(root, pop_fn)