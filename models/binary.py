import sys

class Node:
    def __init__(self, data) -> None:
        self.data:dict = data
        
        self.left:Node = None
        self.right:Node = None
    
    def __repr__(self) -> str:
        return f'<Node {self.data["id"]}>'

class Tree:
    def __init__(self) -> None:
        self.root:Node = None
    
    def _insert(self, data:dict, node:Node):
        if node is None:
            return Node(data)

        elif data['id'] < node.data['id']:
            node.left = self._insert(data, node.left)
        else:
            node.right = self._insert(data, node.right)
        
        return node

    def insert(self, data:dict) -> None:
        if self.root is None:
            self.root = Node(data)
        
        else:
            self._insert(data, self.root)

    def _check_data_node(self,rdata:dict,data:dict) -> bool:
        def check_type(value):
            if type(value) == str:
                return f'"{value}"'
            
            if type(value) == int or type(value) == float:
                return value
            
            raise ValueError(f'Data type {type(value)} not indentified')
        
        return all([eval(f'{check_type(rdata[i])}{data[i][1]}{check_type(data[i][0])}') for i in data.keys()])

    def _preorder(self, root:Node, filter:dict={}) -> list:
        res = []
        if root:
            if filter:
                if self._check_data_node(root.data,filter):
                    res.append(root.data)
            else:
                res.append(root.data['id'])
            
            res += self._preorder(root.left,filter)
            res += self._preorder(root.right,filter)

        return res
    
    def preorder(self) -> None: # Root -> Left -> Right
        return self._preorder(self.root)
    
    def available_data(self) -> list:
        return list(self.root.data.keys())

    def filter_by(self,data:dict) -> list:
        return self._preorder(self.root,data)


    def _ptree(self, node:Node, indent:str, last:bool) -> None:
        if node is not None:
            sys.stdout.write(indent)
            
            if last:
                sys.stdout.write("R----")
                indent += "     "
            
            else:
                sys.stdout.write("L----")
                indent += "|    "
            
            print(node.data['id'])
            
            self._ptree(node.left, indent, False)
            self._ptree(node.right, indent, True)

    def ptree(self):
        return self._ptree(self.root, "",True)