""" adapted from
https://realpython.com/linked-lists-python/ """

# class
class LinkedList(object):
    # ctor
    def __init__(self, nodes=None):  # if no nodes passed, nodes = None
        self.head = None
        # if nodes were passed, then create Node(s) and add them to list in the order starting at index 0.
        if nodes is not None:
            # set first node to head
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # nicer printing to screen
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:  # create list with the data in all nodes
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        # e.g. h -> e -> l -> l -> o -> None, for those letters added in order from left to right.
        return " -> ".join(nodes)

class Node(object):
    # ctor
    def __init__(self, data):
        self.data = data
        self.next = None

    # special method overriding Py default
    def __repr__(self):
        return str(self.data)
    # inst methods
    # def del
