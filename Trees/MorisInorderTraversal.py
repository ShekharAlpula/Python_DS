from Utils import TreeNode, TreeUtils

def morrisInorderTraversal(root: TreeNode):
    while root is not None:
        if root.left is None:
            print(root.value, end=" ")
            root = root.right
        else:
            temp = root.left
            while temp.right is not None and temp.right != root:
                temp = temp.right
            
            if temp.right is None:
                temp.right = root
                root = root.left
            else:
                temp.right = None
                print(root.value, end=" ")
                root = root.right

            
if __name__ == "__main__":
    arr = [1, 2, 4, -1, 7, -1, -1, 5, -1, 6, 8, -1, -1 , -1, 3, -1, -1]
    index = [0]
    root = TreeUtils.buildTree(arr, index)
    print("Level Order Traversal of the tree is:")
    TreeUtils.printLevelOrder(root)
    print("Inorder Traversal of the tree is:")
    morrisInorderTraversal(root)
    print() 

    