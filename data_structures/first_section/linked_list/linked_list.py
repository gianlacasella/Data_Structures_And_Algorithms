

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def set_value(self, value):
        self.value = value
    
    def set_next_node(self, value):
        self.next_node = next_node
    


class Linked_List:
    def __init__(self):
        self.head_node = None

    def __str__(self):
        string = ""
        if self.head_node == None:
            return string
        else:
            reference = self.head_node
            while reference != None:
                string += str(reference.value) + " "
                reference = reference.next_node
            return string

    def add_node_at_head(self, value):
        if self.head_node == None:
            self.head_node = Node(value, None)
        else:
            self.head_node = Node(value, self.head_node)

    def add_node_at_tail(self, value):
        if self.head_node == None:
            self.head_node = Node(value, None)
        else:
            reference = self.head_node
            while reference.next_node != None:
                reference = reference.next_node
            reference.next_node = Node(value, None)
    
    def insert_node_at_index(self, value, index):
        pass
    

llist = Linked_List()
print(llist)
llist.add_node_at_head(2)
print(llist)
llist.add_node_at_head(3)
print(llist)
llist.add_node_at_tail(3)
print(llist)