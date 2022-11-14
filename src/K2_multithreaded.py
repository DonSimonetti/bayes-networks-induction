import multiprocessing

import pandas

from gFunction import g_function
from multiprocessing import Process, Manager
from node import Node


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
    k2_threads = []
    managed_nodes_dict = Manager().dict(nodes_dict)
    for node_name in order_array:
        thrd = Process(target=k2_on_node, args=(cases_set, max_parents, node_name, managed_nodes_dict, order_array))
        k2_threads.append(thrd)
        thrd.start()

    [thrd.join() for thrd in k2_threads]
    return managed_nodes_dict


_print_lock = multiprocessing.Lock()
_iteration_counter = Manager().Value(value=0, typecode=int)


def k2_on_node(cases_set, max_parents, node_name: str, nodes_dict, order_array):
    pi = set()
    old_prob = g_function(nodes_dict[node_name], pi, cases_set)
    ok_to_proceed = True
    while ok_to_proceed and len(pi) < max_parents:

        pred_minus_pi = predecessors(nodes_dict[node_name], nodes_dict, order_array) - pi
        node_z, new_prob = get_node_that_maximises_g(nodes_dict[node_name], pred_minus_pi, pi, cases_set)

        if new_prob > old_prob:
            old_prob = new_prob
            pi.add(node_z.var_name)
        else:
            ok_to_proceed = False

    # "write node and its parents"
    new_node = Node(node_name, nodes_dict[node_name].var_domain)
    new_node.parents = pi
    nodes_dict[node_name] = new_node
    ###

    with _print_lock:
        _iteration_counter.set(_iteration_counter.get() + 1)
        print("[", _iteration_counter.get(), "] K2 on node", node_name, "done")
