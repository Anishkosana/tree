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
     #This function will call insert method for each element to build tree 
    def build(self,nums):
        
        root=None
        
        for num in nums:
            root=self.insert(root,num)
        
        return root
    
    # Merging two functions into a single function
    def Build_BST(self,nums):
        root=None
        for num in nums:
            if root is None:
                root=Node(num)
            continue
            
            curr=root
            parent=None
            
            while curr:
                parent=curr
                
                if num<curr.val:
                    curr=curr.left
                
                else:
                    curr=curr.right
            
            if num<parent.val:
                parent.left=Node(num)
            
            else:
                parent.right=Node(num)
        
        return root
    # Recursive method for building BST
    
    def RBuild_BST(self,nums):
        root=None
        # This function insert each element
        def insert(root,num):
            if not root:
                return Node(num)
            if num<root.val:
                root.left=insert(root.left,num)
            
            else:
                root.right=insert(root.right,num)
                
            return root
        
        for num in nums:
            root=insert(root,num)
        
        return root
    
Tree=BST()
nums=[10,5,15,7,9]
Tree.build(nums)
Tree.Build_BST(nums)