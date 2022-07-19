import pandas

from src.node import Node
from gFunction import g_function
import numpy


def get_node_that_maximises_g(node: Node, parents_set: set, nodes_dict: dict, nodes_order, cases_set: pandas.DataFrame):
    predecessors_of_node = predecessors(node, nodes_dict, nodes_order)
    predecessors_of_node = predecessors_of_node - parents_set

    max_g_node = None
    max_g_value = 0
    for node_z in predecessors_of_node:
        value = g_function(node, parents_set.union({node_z.var_name}), cases_set)
        if value > max_g_value:
            max_g_value = value
            max_g_node = node_z

    return max_g_node, max_g_value


def predecessors(node: Node, nodes_dict: dict, nodes_order) -> set:
    pred = set()
    for i in nodes_order:
        if i == node.var_name:
            break
        pred.add(nodes_dict[i])

    return pred


def k2_procedure(nodes_dict: dict, order_array, max_parents: int, cases_set) -> dict:
    for node_name in nodes_dict:
        node = nodes_dict[node_name]
        print("k2 on node", node_name)

        pi = set()
        old_prob = g_function(node, pi, cases_set)

        should_exit = False
        while (not should_exit) and (len(pi) < max_parents):

            [node_z, g_value] = get_node_that_maximises_g(node, pi, nodes_dict, order_array, cases_set)

            tmp_parents = pi.copy()
            tmp_parents.add(node_z)
            new_prob = g_value

            if new_prob > old_prob:
                old_prob = new_prob
                pi.add(node_z.var_name)
            else:
                should_exit = True
        node.parents = pi  # "write node and its parents"

    return nodes_dict
