class Node(object):
    def __init__(self):
        self.data = None
        self.next_link = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_link(self):
        return self.next_link

    def set_next_link(self, data):
        self.next_link = data


class LinkedList(object):
    def __init__(self, data):
        self.head = Node()
        self.head.set_data(data)
        self.length = 1

    '''
    This method creates a new Node and set its data to the value that the user would like to append to the linked
    list.  It then sets the connected node to the same one that the header is pointing to. Lastly, it points the head to
    the new node that was created in this method
    '''
    def prepend(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next_link(self.head)
        self.head = temp
        self.length += 1

    '''
    This method creates a new node and assigns the programmers input to the node's data attribute. It then loops through
    the current linked list until it reaches the last node. Once at the last node it assigns the the node's next_link
    attribute as the node that was created at the beginning of this method.
    '''
    def append(self, data):
        temp = self.head
        last_node = Node()
        last_node.set_data(data)

        while temp.get_next_link() is not None:
            temp = temp.get_next_link()

        temp.set_next_link(last_node)

        self.length += 1

    '''
    This method check to ensure that the user enter a valid index to insert the new data into. A valid index is 
    is considered to be any index from the start of the linked list to the end of the linked list. This method will make
    use of the append method if the index selected is at the beginning of the list and it will make use of the prepend
    method if the index entered is the the same as the size of the linked list. If neither of the conditions mentioned
    above aren't met then a new node will be created and the program will loop through the current linked list until 
    it reaches the specified index. It will then connect the remainder of the linked list to the new node and link the 
    beginning of the linked list to the new node.
    '''
    def insert_at_index(self, index, data):
        if index > self.get_length() or index < 0:
            print('You can only insert in this range: %d - %d' % (0, self.get_length()))

        elif index == 0:
            self.prepend(data)

        elif index == self.get_length():
            self.append(data)

        else:
            new_node = Node()
            new_node.data = data
            temp = self.head
            tracker = 0

            while tracker < index - 1:
                temp = temp.get_next_link()
                tracker += 1

            holder = temp.get_next_link()
            temp.set_next_link(new_node)
            new_node.set_next_link(holder)

    '''
    This method loops through the linked list and build a string representation of all the values in the linked list
    then it displays string when all the values from the linked linked list are appended to it.
    '''
    def display(self):
        temp = self.head
        output = ''
        while temp is not None:
            if temp.get_next_link() is not None:
                output += "Name: " + str(temp.get_data().get_name()) + " | Age: " + str(temp.get_data().get_age()) + '->'
            else:
                output += "Name: " + str(temp.get_data().get_name()) + " | Age: " + str(temp.get_data().get_age())
            temp = temp.get_next_link()

        print(output)

    def get_length(self):
        return self.length



