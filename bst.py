class BST:
    def __init__(self, data):
        self.key = data
        self.l_child = None
        self.r_child = None

    def bst_preorder(self):
        print(self.key, end=" ")
        if self.l_child:
            self.l_child.bst_preorder()
        if self.r_child:
            self.r_child.bst_preorder()

    def bst_inorder(self):
        if self.l_child:
            self.l_child.bst_inorder()
        print(self.key, end=" ")
        if self.r_child:
            self.r_child.bst_inorder()

    def bst_postorder(self):
        if self.l_child:
            self.l_child.bst_postorder()
        if self.r_child:
            self.r_child.bst_postorder()
        print(self.key, end=" ")

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.l_child:
                self.l_child.insert(data)
            else:
                self.l_child = BST(data)
        else:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)

    def search(self, data):
        if self.key == data:
            print("Found the element !!!!...")
            return
        if self.key > data:
            if self.l_child:
                self.l_child.search(data)
            else:
                print("The Searching element is not present in the tree")
                return
        else:
            if self.r_child:
                self.r_child.search(data)
            else:
                print("The Searching element is not present in the tree")
                return

    def delete_node(self, val):
        if self.key is None:
            print("tree is Empty")
            return
        if self.key > val:
            if self.l_child:
                self.l_child = self.l_child.delete_node(val)
            else:
                print('Element not found in left')
                return
        elif self.key < val:
            if self.r_child:
                self.r_child = self.r_child.delete_node(val)
            else:
                print('Element not found in right')
                return
        elif self.key == val:
            if self.l_child is None:
                temp = self.r_child
                self = None
                return temp
            if self.r_child is None:
                temp = self.l_child
                self = None
                return temp
            node = self.r_child
            while node.l_child is not None:
                node = node.l_child
            self.key = node.key
            self.r_child = self.r_child.delete_node(node.key)
        return self


if __name__ == "__main__":
    tree = BST(13)
    list1 = [24, 11, 9, 5, 17, 25, 31, 1, 21, 3]
    for i in list1:
        tree.insert(i)
    tree.search(31)
    tree.search(11)
    tree.search(25)
    tree.search(888)
    print("\nThis is inorder traversal")
    tree.bst_inorder()
    print("\nThis is preorder traversal")
    tree.bst_preorder()
    print("\nThis is postorder traversal")
    tree.bst_postorder()
    print("\n\n")
    tree.delete_node(25)
    tree.delete_node(3)
    tree.delete_node(31)
    # tree.delete_node(17)
    tree.delete_node(9)
    tree.delete_node(13)
    tree.delete_node(4)

    print("\nThis is inorder traversal")
    tree.bst_inorder()
    print("\nThis is preorder traversal")
    tree.bst_preorder()
    print("\nThis is postorder traversal")
    tree.bst_postorder()
