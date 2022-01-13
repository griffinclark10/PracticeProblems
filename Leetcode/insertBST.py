#parent = n
#left node = 2n+1
#right node = 2n+2

def insertIntoBST(root: Optional[TreeNode], val: int)->Optional[TreeNode]:
    if root is None: return TreeNode(val) 
    if root.val > val:  root.left = insertIntoBST(root.left, val)
    else: root.right = insertIntoBST(root.right, val)
    return root