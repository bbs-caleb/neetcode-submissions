class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        sum = 0

        def dfs(node):
            nonlocal sum
            if not node:
                return 0
            
            dfs(node.left)
            if low <= node.val <= high:
                sum += node.val
            dfs(node.right)
        dfs(root)
        return sum