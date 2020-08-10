
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

    def remove_head(self):
        if self.head_node == None:
            raise IndexError
        else:
            self.head_node = self.head_node.next_node
    
    def remove_tail(self):
        indx = 0
        if self.head_node == None:
            raise IndexError
        if self.length() == 1:
            self.head_node = None
        else:
            reference = self.head_node
            while indx < self.length()-2:
                reference = reference.next_node
                indx += 1
            reference.next_node = None

    def insert_node_at_index(self, value, index):
        if self.valid_index(index):
            if index == 0:
                self.add_node_at_head(value)
            else:
                aux_indx = 0
                reference = self.head_node
                while aux_indx != index-1:
                    aux_indx += 1
                    reference = reference.next_node
                reference.next_node = Node(value, reference.next_node)
        else:
            raise IndexError

    def remove_node_at_index(self, index):
        if self.valid_index(index):
            if index == 0:
                self.remove_head()
            elif index == self.length()-1:
                self.remove_tail()
            else:
                cnt = 0
                reference = self.head_node
                while cnt <= index - 2:
                    reference = reference.next_node
                    cnt += 1
                reference.next_node = reference.next_node.next_node

    def valid_index(self, index):
        if index not in range(0, self.length()):
            return False
        else:
            return True

    def length(self):
        cnt = 0
        if self.head_node == None:
            return cnt
        else:
            reference = self.head_node
            while reference != None:
                cnt += 1
                reference = reference.next_node
        return cnt
