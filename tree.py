TYPES = ["int", "float", "string"]


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
        if self == None:
            return
        if self.leaf:
            print("  " * (level + 1) + str(self.leaf))
        for child in self.children:
            child.print_tree(level + 1)

    def validate_all_leafs(self, type, variables):
        if (self.type != "ID") and (self.leaf is not None) and (self.type != "NUMBER"):
            return False
        elif self.type == "ID":
            scope_id = self.children[0].leaf
            variable_type = variables[(self.leaf, scope_id)]

            if variable_type != type and type in TYPES:
                return False
        elif self.type == type:
            return True
        elif self.type != type:
            return False
        else:
            for child in self.children:
                if not child.validate_all_leafs(type, variables):
                    return False

        return True
