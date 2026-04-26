class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        
        def build(start, end):
            if start > end:
                return [None]
            
            trees = []
            
            for root_val in range(start, end + 1):
                left_subtrees = build(start, root_val - 1)
                right_subtrees = build(root_val + 1, end)
                
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            
            return trees
        
        return build(1, n)