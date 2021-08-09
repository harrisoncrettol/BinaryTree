class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = Node(None)

        #test purpose lists
        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []
    
    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)


def main():
    tree = BinaryTree()
    nums = [5,3,7,9,8,6,2,4]
    
    for num in nums:
        tree.add(num)

    print(tree.head.val)



if __name__ == "__main__":
    main()
