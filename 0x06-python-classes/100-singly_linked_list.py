#!/usr/bin/python3
"""An empty 'class Square' here"""


class Node:
    """ A square is a four-sided shape"""
    def __init__(self, data, next_node=None):
        """Contructor set up goes here..."""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list class"""
    def __init__(self):
        """Linked List init?"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting new node"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Handles print format for SinglyLinkedList"""
        res = []
        temp = self.__head
        while temp is not None:
            res.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(res)
