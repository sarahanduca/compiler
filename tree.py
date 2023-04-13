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

    def validate_all_leafs(self,type,variables):
        if (self.type != 'term') and (self.leaf is not None) and (self.type != type) and self.type != "expression":
            return False
        elif self.type == "term":
            scope_id  = self.children[0].leaf
            variable_type = variables[(self.leaf,scope_id)]
            if variable_type not in TYPE_MAPE[type]:
                return False
        elif(self.type == type):
            return True
            
        else:
            for child in self.children:
                if not child.validate_all_leafs(type,variables):
                    return False       
        return True
