#!/usr/bin/python3
"""Node class represents a node of a singly linked list"""


class Node:
    """
    Node class represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object with the given data and next_node.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the linked list.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data value of the node.

        Args:
            value (int): The new data value of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList object.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
