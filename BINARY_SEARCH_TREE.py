class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
class BST:
    
    # iterative method of building bst
    def insert(self,root,key):
        
        if not root:
            return Node(key)
        
        curr=root
        parent=None
        
        while curr:
            parent=curr
            
            if curr.val<key:
                curr=curr.left
            
            else:
                curr=curr.right
                
        if key<parent.val:
            parent.left=Node(key)
        
        else:
            parent.right=Node(key)
            
        return root
        
    def build(self,nums):
        
        root=None
        
        for num in nums:
            root=self.insert(root,num)
        
        return root