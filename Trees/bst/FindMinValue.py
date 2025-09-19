import sys

# Add the path to the directory containing the Utils module
sys.path.append(r"C:/WorkSpace/Programs/Python/DS/Trees/")
from Utils import TreeNode, TreeUtils

def findMinValue(root: TreeNode) -> int:
    if root is None:
        return sys.maxsize
    
    while root.left is not None:
        root = root.left

    return root.value

def findMaxValue(root : TreeNode) -> int:
    if root is None :
        return -sys.maxsize
    while root.right is not None:
        root = root.right
    
    return root.value


if __name__ == "__main__":
    arr = [5, 3, 2, -1, -1, 4, -1, -1, 8, -1, 9, -1, -1]
    index = [0]
    root = TreeUtils.buildTree(arr, index)
    print("Level Order Traversal of the tree is:")
    TreeUtils.printLevelOrder(root)
    print("Minimum value in the BST is:", end=" ")
    print(findMinValue(root))
    print()
    print("Maximum value in the BST is:", end=" ")
    print(findMaxValue(root))
    print()



