class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def __str__(self):
        return self.type

    def print_tree(self, level=0):
        print("  " * level + str(self))
        if self.leaf:
            print("  " * (level + 1) + str(self.leaf))
        for child in self.children:
            child.print_tree(level + 1)

    # def verify_type(type, value):
