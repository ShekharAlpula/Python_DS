
from collections import deque
from Utils import TreeNode, TreeUtils


def leftView(root: TreeNode):
    if root is None:
        return
    Q = deque()
    Q.append(root)

    while Q:
        size = len(Q)
        for i in range(size):
            node = Q.popleft()
            if i == 0 :
                print(node.value, end="  ")
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
            
def rightView(root: TreeNode):
    if root is None:
        return
    Q = deque()
    Q.append(root)

    while(Q):
        size = len(Q)
        for i in range(size):
            node = Q.popleft()
            if i == size -1:
                print(node.value, end="  ")
            if node.left is not None:
                Q.append(node.left)
            if node.right is not None:
                Q.append(node.right)

    
def bottomView(root: TreeNode):
    if root is None:
        return    
    Q = deque()
    Q.append((root, 0))
    hd_map = {}

    while Q:
        node = Q.popleft()
        hd = node[1]
        hd_map[hd] = node[0].value
        if node[0].left is not None:
            Q.append((node[0].left, hd - 1))
        if node[0].right is not None:
            Q.append((node[0].right, hd + 1))

    for i in sorted(hd_map.keys()):
        print(hd_map[i], end="  ")

def top_view(root: TreeNode):
    if root is None:
        return    
    Q = deque()
    Q.append((root, 0))
    hd_map = {}

    while Q:
        node = Q.popleft()
        hd = node[1]
        if hd not in hd_map:
            hd_map[hd] = node[0].value
        if node[0].left is not None:
            Q.append((node[0].left, hd - 1))
        if node[0].right is not None:
            Q.append((node[0].right, hd + 1))

    for i in sorted(hd_map.keys()):
        print(hd_map[i], end="  ")
        
if __name__ == "__main__":
    arr = [5, 4, 11, 7, 6, -1, -1, -1, 2, -1, -1, -1, 8, 13, -1 , -1, 9, -1, 1, -1, -1];
    index = [0]
    root = TreeUtils.buildTree(arr, index)
    print("Left view- of tree is:")
    leftView(root)
    print("\nRight view- of tree is:")
    rightView(root)
    print("\nBottom view- of tree is:")
    bottomView(root)
    print()

