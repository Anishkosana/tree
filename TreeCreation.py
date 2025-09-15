# Expermenting with git

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def build_tree(self,elements,index=0):
        if index>=len(elements):
            return None
        
        node=TreeNode(elements[index])
        node.left=self.build_tree(elements,2*index+1)
        node.right=self.build_tree(elements,2*index+2)
        return node
    
    # This version only build the left skewed tree
    
    # def build_tree_al(self,elements):
    #     if not elements:
    #         return None
        
    #     val=elements.pop(0)
    #     node=TreeNode(val)
        
    #     if elements:
    #         node.left=self.build_tree_al(elements)
    #     if elements:
    #         node.right=self.build_tree_al(elements)
    #     return node
    
    # iterative version of building tree
    
    def build_binary_tree_iteration(self,elements):
        if not elements:
            return None
        
        root=TreeNode(elements[0])
        stack=[root]
        i=1
        while i<len(elements):
            current=stack.pop(0)
            if i<len(elements):
                current.left=TreeNode(elements[i])
                stack.append(current.left)
            i+=1
            if i<len(elements):
                current.right=TreeNode(elements[i])
                stack.append(current.right)
            i+=1
        return root
        
elements=[1,2,3,4,5,6,7,8]
tree=Tree()
root=tree.build_binary_tree_iteration(elements)
# root2=tree.build_tree_al(elements)
