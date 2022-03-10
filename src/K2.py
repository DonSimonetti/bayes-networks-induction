from node import Node


def g_function(node, parents, case_set):  # TODO
    prob = 0.0

    return prob


def K2(nodes_array, order_array, max_parents, cases_database):  # TODO

    for i in order_array:
        node = nodes_array[order_array[i]]
        pi = []

        old_prob = g_function(node, pi, cases_database)

        should_exit = False
        while (not should_exit) and (len(pi) < max_parents):
            Z = Node()
            # TODO find node Z in 'nodes_array[i].parents \ pi' such that maximise g_function(Z,pi)

            new_prob = g_function(node, pi.copy().append(Z), cases_database)
            if new_prob > old_prob:
                old_prob = new_prob
                pi.append(Z)
            else:
                should_exit = True
        node.parents = pi  # "write node and its parents"

    return nodes_array
