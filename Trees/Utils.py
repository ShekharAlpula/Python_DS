from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)
    def __str__(self):
        return str(self.value)

class TreeUtils:
    @staticmethod
    def buildTree(values : list, index=[0]):
        if index[0] >= len(values) or values[index[0]] == -1 :
            index[0] += 1
            return None
        
        data = values[index[0]]  
        root = TreeNode(data)
        index[0] += 1
        root.left = TreeUtils.buildTree(values, index)
        root.right = TreeUtils.buildTree(values, index)

        return root;

    @staticmethod
    def printLevelOrder(root: TreeNode):
        if not root:
            return
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                print(node.value, end="  ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append( node.right)

            print()


def LevelOrderTraversal(root: TreeNode):
    if not root:
        return
    Q = deque()
    Q.append(root)
    while Q :
        size = len(Q)
        for i in range(size):            
            node = Q.popleft()
            print(node.value, end="  ")
            if node.left is not None:
                Q.append(node.left)
            if node.right is not None:
                Q.append(node.right)
        print()
            

def test():
    arr = [5, 4, 11, 7, 6, -1, -1, -1, 2, -1, -1, -1, 8, 13, -1 , -1, 4, -1, 1, -1, -1];
    index = [0]
    root = TreeUtils.buildTree(arr, index)
    print("Level Order Traversal of the tree is:")
    TreeUtils.printLevelOrder(root)

    print("Level Order Traversal of the tree is:")
    LevelOrderTraversal(root)


if __name__ == "__main__":
    test()