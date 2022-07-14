class Node:

    def __init__(self, name, possible_values):
        self.var_name = name
        self.parents = set()
        self.var_domain = possible_values
        return
