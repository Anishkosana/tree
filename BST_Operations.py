import BINARY_SEARCH_TREE as bst

class BST_OPERATION:
    #Iterative search
    def ISearch(self,root,key):
        
        if not root:
            return None
        
        t=root
        
        while t:
            
            if t.val==key:return  t
            
            if t.val>key:t=t.left
            
            else:t=t.right
            
        return None
                   
    #Recursive search
    def RSearch(self,root,key):
        
        if not root: return None
        
        if root.val==key: return root
                    
        if key<root.val:
            return self.RSearch(root.left,key)
        else:
            return self.RSearch(root.right,key) 
        
    # Inorder Traversal
    def Inorder(self,root):
        if not root: return None
        
        self.Inorder(root.left)
        print(root.val,end="->")
        self.Inorder(root.right)  
    
    #Iterative insert
    def IInsert(self,root,key):
        r=None
        t=root
        while t:
            r=t
            if key==t.val:return
            
            elif key<t.val:t=t.left
            else:t=t.right
        
        n=bst.Node(key)
        if n.val<r.val:r.left=n 
        else: r.right=n
    
    #Recursive insert
    def RInsert(self,root,key):
        if not root:
            return bst.Node(key)
        if root.val==key:
            return None
        if key<root.val:
            root.left=self.RInsert(root.left,key)
        else:
            root.right=self.RInsert(root.right,key)
        
        return root
    # finding minimum difference
    def getMin_diff(self,root):
        prev,min_diff=None,1000
        stack,current=[],root
        
        while stack or current:
            
            while current:
                stack.append(current)
                current=current.left
            
            current=stack.pop()
            
            if prev is not None:
                diff=current.val-prev
                if diff<min_diff:
                    min_diff=diff
            prev=current.val
            current=current.right
        return min_diff 
        
op=BST_OPERATION()
# print(op.ISearch(bst.root,7))
# print(op.RSearch(bst.root,7))

# op.IInsert(bst.root,2)
# op.RInsert(bst.root,2)
# op.Inorder(bst.root)
print("Minimum difference : ",op.getMin_diff(bst.root))
