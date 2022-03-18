class Node:

    def __init__(self, name, possible_values):
        self.var_name = name
        self.parents = set()
        self.var_domain = possible_values
        self.var_domain_size = len(self.var_domain)  # I.E. the r_i possible value assignments
        return
