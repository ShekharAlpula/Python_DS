from Utils import TreeNode, TreeUtils

def findLCA(root: TreeNode, a: int, b: int) -> TreeNode:
    if root is None:
        return None
    if root.value > a and root.value > b:
        return findLCA(root.left, a, b)
    if root.value < a and root.value < b:
        return findLCA(root.right, a, b)
    return root

if __name__ == "__main__":
    arr = [8,3,1,-1, -1, 6, 4, -1, -1, 7, -1, -1, 10, -1, 14, 13, -1, -1, -1]
    index = [0]
    root = TreeUtils.buildTree(arr, index)
    print("Level Order Traversal of the tree is:")
    TreeUtils.printLevelOrder(root)
    a = 1
    b = 7    

    node = findLCA(root, a, b)
    if node is not None:
        print(f"LCA of {a, b}:", node.value)
    else:   
        print(f"LCA of {a, b}:", )

