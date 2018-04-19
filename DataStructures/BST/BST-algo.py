class BST(object):
    def __init__(self, root_val):
        self.data = root_val
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        elif value > self.data:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if self.data == value:
            print('The BST contains ' + str(value) + '.')
            return True
        elif self.data >= value and self.left is not None:
            self.left.contains(value)
        elif self.data < value and self.right is not None:
            self.right.contains(value)
        else:
            print('The BST does not contain: ' + str(value) + '.')
            return False

    def print_inorder(self):
        if self.left is not None:
            self.left.print_inorder()

        print(self.data)

        if self.right is not None:
            self.right.print_inorder()


    def print_preorder(self):
        print(self.data)
        if self.left is not None:
            self.left.print_preorder()

        if self.right is not None:
            self.right.print_preorder()

    def print_postorder(self):

        if self.left is not None:
            self.left.print_postorder()

        if self.right is not None:
            self.right.print_postorder()


        print(self.data)


if __name__ == '__main__':
    my_bst = BST(1)
    my_bst.insert(2)
    my_bst.insert(3)
    my_bst.insert(4)
    my_bst.insert(5)

    print('inorder')
    my_bst.print_inorder()
    print('preorder')
    my_bst.print_preorder()
    print('postorder')
    my_bst.print_postorder()
