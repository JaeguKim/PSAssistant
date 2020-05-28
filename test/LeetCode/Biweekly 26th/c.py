# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recursion(parent,maxVal,res,total):
    if parent == None:
        return
    if parent.val < maxVal:
        res[0]+=1
    else:
        maxVal = parent.val
    total[0] +=1
    recursion(parent.left,maxVal,res,total)
    recursion(parent.right,maxVal,res,total)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        total = [1]
        maxVal = root.val
        if root.left == None and root.right == None:
            return 1
        recursion(root.left,maxVal,res,total)
        maxVal = root.val
        recursion(root.right,maxVal,res,total)
        return total[0]-res[0]