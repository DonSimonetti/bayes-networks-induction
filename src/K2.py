import pandas

from node import Node
from gFunction import g_function
import numpy


# nodes_set should be 'pred(node) - pi'
def get_node_that_maximises_g(node: Node, nodes_set, parents_set: set, cases_set: pandas.DataFrame):
    max_g_node = None
    max_g_value = 0

    for node_z in nodes_set:
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


def k2_procedure(nodes_dict: dict, order_array, max_parents: int, cases_set: pandas.DataFrame) -> dict:
    iteration = 1
    for node_name in order_array:
        ##
        node = nodes_dict[node_name]
        print("[", iteration, "] K2 on node", node_name)
        iteration += 1
        ##

        pi = set()
        old_prob = g_function(node, pi, cases_set)

        ok_to_proceed = True
        while ok_to_proceed and len(pi) < max_parents:

            pred_minus_pi = predecessors(node, nodes_dict, order_array) - pi
            node_z, new_prob = get_node_that_maximises_g(node, pred_minus_pi, pi, cases_set)

            if new_prob > old_prob:
                old_prob = new_prob
                pi.add(node_z.var_name)
            else:
                ok_to_proceed = False
        node.parents = pi  # "write node and its parents"

    return nodes_dict
