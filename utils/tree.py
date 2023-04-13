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
        if (
            (self.type != "ID")
            and (self.leaf is not None)
            and (self.type != "NUMBER")
            and (self.type != "expression")
            and (self.type != "factor")
            and (self.type != type)
        ):
            return False
        elif self.type == "ID":
            scope_id = self.children[0].leaf
            variable_type = variables[(self.leaf, scope_id)]

            if variable_type != type and type not in TYPES:
                return False
        elif self.type == type:
            return True
        else:
            for child in self.children:
                if not child.validate_all_leafs(type, variables):
                    return False

        return True

    def validate_type(self, type, variables):
        if self == None:
            return False

        elif self.type == "ID":
            scope_id = self.children[0].leaf
            variable_type = variables[(self.leaf, scope_id)]

            if variable_type == type and type in TYPES:
                return True

        elif self.type == "type":
            return self.children[0].validate_type(type, variables)

        elif self.type == "var_type" and self.leaf == type:
            return True

        elif self.type == type:
            return True

        else:
            for child in self.children:
                isType = child.validate_type(type, variables)
                if isType:
                    return True

        return False

    def is_zero(self):
        if self.type == "type":
            return False
        if self.type == "NUMBER":
            if self.leaf - 0 == 0:
                return True
        else:
            for child in self.children:
                isZero = child.is_zero()
                if isZero:
                    return True
        return False
