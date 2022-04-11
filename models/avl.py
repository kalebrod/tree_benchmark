from models.binary import Node, Tree

class AVLNode(Node):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.height = 1

    def __repr__(self) -> str:
        return f'<AVLNode {self.data["id"]}>'
    
class AVLTree(Tree):
    def __init__(self) -> None:
        super().__init__()

    def getHeight(self, node:AVLNode) -> int:
        if not node:
            return 0

        return node.height

    def getBalance(self,node) -> int:
        if not node:
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right)

    def _leftRotate(self, node:AVLNode) -> AVLNode:
        new = node.right
        node.right = node.right.left
        new.left = node

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        new.height = 1 + max(self.getHeight(new.left),self.getHeight(new.right))
        
        return new

    def _rightRotate(self, node:AVLNode) -> AVLNode:
        new = node.left
        node.left = node.left.right
        new.right = node

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        new.height = 1 + max(self.getHeight(new.left),self.getHeight(new.right))
        
        return new

    # Function to insert a node
    # Override base function
    def _insert(self, data:dict, node:AVLNode):
        if node is None:
            return AVLNode(data)

        elif data['id'] < node.data['id']:
            node.left = self._insert(data,node.left)

        else:
            node.right = self._insert(data,node.right)

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))

        balanceFactor = self.getBalance(node)

        if balanceFactor > 1:
            if data['id'] < node.left.data['id']:
                return self._rightRotate(node)
            else:
                node.left = self._leftRotate(node.left)
                return self._rightRotate(node)

        if balanceFactor < -1:
            if data['id'] > node.right.data['id']:
                return self._leftRotate(node)
            else:
                node.right = self._rightRotate(node.right)
                return self._leftRotate(node)
        
        return node

    def insert(self, data:dict) -> None:
        if self.root is None:
            self.root = AVLNode(data)
        
        else:
            return self._insert(data, self.root)