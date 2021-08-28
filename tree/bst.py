
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _add(self, node, val):

        if node == None:
            return Node(val)
        if node.val > val:
            if node.left == None:
                node.left = Node(val)
            node.left = self._add(node.left, val)
        elif node.val < val:
            if node.right == None:
                node.right = Node(val)
            node.right = self._add(node.right, val)
        return node

    def add(self, val):

        self.root = self._add(self.root, val)

    def findMin(self):
        cur = self.root
        if not cur:
            return
        while cur.left != None:
            cur = cur.left

        return cur.val

    def findMax(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.val

    def _find(self, node, val):
        if node == None:
            return False
        if node.val == val:
            return True
        if node.val > val:
            return self._find(node.left, val)
        if node.val < val:
            return self._find(node.right, val)

    def find(self, val):
        return self._find(self.root, val)

    def findMinNode(self, node):
        while node.left:

            node = node.left
        return node.val

    def _remove(self, root, val):

        if root is None:
            return root

        if val < root.val:
            root.left = self._remove(root.left, val)

        elif(val > root.val):
            root.right = self._remove(root.right, val)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            minVal = self.findMinNode(root.right)

            root.val = minVal

            root.right = self._remove(root.right, minVal)

        return root

    def remove(self, val):
        if self.root == None:
            return

        self.root = self._remove(self.root, val)

        return self.root

    def _height(self, node):
        if node == None:
            return 0
        left = self._height(node.left)
        right = self._height(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def height(self):
        return self._height(self.root)

    def _minHeight(self, node):
        if node == None:
            return 0
        left = self._height(node.left)
        right = self._height(node.right)
        if left < right:
            return left + 1
        else:
            return right + 1

    def minHeight(self):
        return self._minHeight(self.root)

    def balanced(self):
        return self.minHeight() >= (self.height() - 1)

    def _inorder(self, node, inorder):
        if not node:
            return
        self._inorder(node.left)
        inorder.append(node.val)
        self._inorder(node.right)

    def inorder(self):
        inorder = []
        self._inorder(self.root, preorder)
        return inorder

    def _preorder(self, node, preorder):
        if not node:
            return
        preorder.append(node.val)
        self._preorder(node.left)
        self._preorder(node.right)

    def preorder(self):
        preorder = []
        self._preorder(self.root, preorder)
        return preorder

    def _postorder(self, node, postorder):
        if not node:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        postorder.append(node.val)

    def postorder(self):
        postorder = []
        self._postorder(self.root, postorder)
        return postorder

    def levelorder(self):

        queue = []
        levelorder = []

        if not self.root:
            return levelorder
        queue.append(self.root)
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            levelorder.append(cur.val)
        return levelorder


bst = BST()
bst.add(5)
bst.add(1)
bst.add(3)
bst.add(2)
bst.add(10)
bst.add(11)
bst.add(8)
# print(bst.root.val)
print(bst.findMin())
print(bst.findMax())
print(bst.levelorder())
bst.remove(1)
print(bst.levelorder())
print(bst.findMin())
print(bst.findMax())
bst.remove(11)
print(bst.levelorder())
print(bst.findMin())
print(bst.findMax())
