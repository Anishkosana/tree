# Expermenting with different branches

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
    
    # inorder iterative version    
    def inorder_itr(self,root):
        
        if not root:
            return 
        
        stack=[]
        current=root
        while stack or current:
            if current:
                stack.append(current)
                current=current.left
            
            else:
                current=stack.pop()
                print(current.val,end="->")
                current=current.right
    
    #preorder iterative version
    def preorder_itr(self,root):
        
        if not root:
            return 
        stack=[root]
        while stack:
            node=stack.pop()
            print(node.val,end="->")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    #postorder iterative version
    def postorder_itr(self,root):
        
        if not root:return
        
        stack=[root]
        out=[]
        
        while stack:
            node=stack.pop()
            out.append(node.val)
            
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
                
        while out:
            print(out.pop(),end="->")
        
    #levelorder iterative version
    def levelorder_itr(self,root):
        if not root:return
        
        queue=[root]
        
        while queue:
            node=queue.pop(0)
            print(node.val,end="->")
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
    #counting nodes of a tree (recursive)
    def count_nodes(self,root):
        if not root:
            return 0
        
        return self.count_nodes(root.left)+self.count_nodes(root.right)+1
      
    #iterative version of counting nodes   
    def count_n_itr(self,root):
        if not root: return 0
        
        stack=[root]
        count=0  
        
        while stack:
            current=stack.pop()
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            
            count+=1
        return count
    #counting leaf nodes
    def leaf_nodes(self,root):
        if not root: return 0
        
        if not root.left and not root.right:
            return 1
        
        return self.leaf_nodes(root.left)+self.leaf_nodes(root.right)
        
op=operation()
# elements=[1,2,3,4,5,6,7,8]
# tree=tc.Tree()
# node=tree.build_binary_tree_iteration(elements)

# op.inorder_itr(tc.root)

# print()

# op.preorder_itr(tc.root)

# print()

# op.postorder_itr(tc.root)

# print()

# op.levelorder_itr(tc.root)
print(op.leaf_nodes(tc.root))




    
        
