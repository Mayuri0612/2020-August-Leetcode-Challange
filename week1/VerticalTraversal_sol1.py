
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def verticalOrder(root, hd, m):
    if root is None:
        return

    #m.setdefault(hd, []).append(root.data)
    if hd in m:
        m[hd].append(root.val)
    else:
        m[hd] = [root.val]

    verticalOrder(root.left, hd-1, m)
    verticalOrder(root.right, hd+1, m)

def printOrder(root):
    m = dict()
    hd = 0
    result  = []
    verticalOrder(root, hd, m)
    
    #traverse map and print node at every horizontal distance
    for i in sorted(m.keys()):
        if i in m:
            result.append([x for x in (m[i])])
    print(result)

if __name__ == '__main__':

    root = Node(0)
    root.left = Node(5)
    root.left.left = Node(9)
    root.right = Node(1)
    root.right.left = Node(2)
    root.right.left.right = Node(3)
    root.right.left.right.left = Node(4)
    root.right.left.right.right = Node(8)
    root.right.left.right.left.left = Node(6)
    root.right.left.right.left.left.left = Node(7)

    printOrder(root)