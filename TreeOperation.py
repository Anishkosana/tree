import TreeCreation as tc

class operation:
    
    # inorder traversal
    def inorder(self,node):
        if not node:
            return None
        
        self.inorder(node.left)
        print(node.val,end="->")
        self.inorder(node.right)
        
    # preorder traversal
    def preorder(self,node):
        
        if not node:
            return None
        
        print(node.val,end="->")
        self.preorder(node.left)
        self.preorder(node.right)
        
    # postorder traversal
    def postorder(self,node):
        
        if not node:
            return None
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val,end="->")
    

op=operation()
print("inorder traversal!!")
op.inorder(tc.root)
print()
print("preorder traversal!!")
op.postorder(tc.root)
print()
print("postorder!!")
op.postorder(tc.root)

    
        
