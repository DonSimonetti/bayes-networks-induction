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


def find_node_that_maximise_g(nodes_set: set, parents_set: set, cases_set: pandas.DataFrame):  # FIXME need testing
    # find node_z in nodes_set (i.e. 'nodes_array[i].parents - pi')
    # such that maximise g_function(node_z, pi+[node_z])

    max_g = 0
    max_g_node = 0
    for i in nodes_set:
        tmp_set = parents_set.copy()
        tmp_set.add(i.var_name)
        tmp = g_function(i, tmp_set, cases_set)
        if tmp > max_g:
            max_g = tmp
            max_g_node = i

    return max_g_node


def predecessors(node: Node, nodes_dict: dict, nodes_order) -> set:

    pred = set()
    for i in nodes_order:
        if i == node.var_name:
            break
        pred.add(nodes_dict[i])

    return pred


# FIXME no parents are being found
def k2_procedure(nodes_dict: dict, order_array, max_parents: int, cases_set) -> dict:
    for node_name in nodes_dict:
        node = nodes_dict[node_name]
        print("k2 on node", node_name)

        pi = set()
        old_prob = g_function(node, pi, cases_set)

        should_exit = False
        while (not should_exit) and (len(pi) < max_parents):

            # preds = predecessors(node, nodes_dict, order_array)
            # preds_minus_pi = preds - pi
            # node_z = find_node_that_maximise_g(preds_minus_pi, pi, cases_set)  # FIXME
            #assert node_z != 0  # what if 'preds - pi' is empty' ?? FIXME

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
