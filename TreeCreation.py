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
    def build_tree_al(self,elements):
        if not elements:
            return None
        
        val=elements.pop(0)
        node=TreeNode(val)
        
        if elements:
            node.left=self.build_tree_al(elements)
        if elements:
            node.right=self.build_tree_al(elements)
        return node

elements=[1,2,3,4,5,6,7]
tree=Tree()
root=tree.build_tree(elements)
