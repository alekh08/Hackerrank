
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def checkBST(root):
    return check_BST_subtree(root, -1, 10001)    
    
def check_binary_search_tree_(root):
    def inorder(r):
        return inorder(r.left) + [r.data] + inorder(r.right) if r else []
    
    res = inorder(root)
    return res == sorted(res) and len(set(res)) == len(res)
