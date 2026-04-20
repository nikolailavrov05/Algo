from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(9)
root.left = TreeNode(16)
root.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.right = TreeNode(11)

def Obhodvshirinu(root):
    if not root:
        return None
    result = []
    queue = deque([root])
    flag = True
    while flag:
        size_of_shirina = len(queue)
        current_shirina = []
        flag = False
        for i in range(size_of_shirina):
            node = queue.popleft()
            current_shirina.append(node.val)
            if node.left is not None:
                queue.append(node.left)
                flag = True
            if node.right is not None:
                queue.append(node.right)
                flag = True
        result.append(current_shirina)
    return result

print(Obhodvshirinu(root))
