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
        
op=BST_OPERATION()
print(op.ISearch(bst.root,7))
print(op.RSearch(bst.root,7))