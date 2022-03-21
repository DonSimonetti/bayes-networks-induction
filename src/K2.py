import math

from src.node import Node
from src.myFactorial import factorial


#  'node_i'     is a Node from node.py
#  'cases_df'   is a pandas DataFrame

def g_function(node_i: Node, parents, cases_df):  # FIXME need testing

    # print("v_i =", node_i.var_domain, "=> r_i =", len(node_i.var_domain))
    # print("pi_i =", parents)

    parents_i_distinct_occurrences = []
    for i in cases_df.filter(items=parents).values.tolist():
        if i not in parents_i_distinct_occurrences:
            parents_i_distinct_occurrences.append(i)

    # print("W_i =", parents_i_distinct_occurrences, "=> q_i =", len(parents_i_distinct_occurrences))

    # print("selecting the columns", parents, ", {'" + node_i.var_name + "'}")
    # for i in cases_df.filter(items=parents.union([node_i.var_name])).values.tolist():
    # print(i)

    N_ij = [0 for j in range(len(parents_i_distinct_occurrences))]

    # PT_j is the vector of the last production term for each j
    PT_j = []

    for j in parents_i_distinct_occurrences:
        # print("for j =", j)
        N_ijk = []
        for k in node_i.var_domain:
            # print("\tcalculating N_ij set where '" + node_i.var_name + "' =", k, "( more precisely N_ijk where k =", k,
            #      ")")
            pi_i_instances = cases_df.filter(items=parents) \
                .where(cases_df[node_i.var_name] == k).copy().dropna().values.tolist()

            # re-cast to int
            for i in pi_i_instances:
                for _j in range(len(i)):
                    i[_j] = int(i[_j])
            #

            # print("\t", pi_i_instances)
            N_ijk.append(pi_i_instances.count(j))

        # now that we have N_ijk for each possible k value of node_i,
        # we calculate their factorials, and multiply them
        N_ij[parents_i_distinct_occurrences.index(j)] = sum(N_ijk)
        # print("N_ijk =", N_ijk, "=> N_ij becomes:", N_ij)
        PT_j.append(math.prod([math.factorial(i) for i in N_ijk]))
        # print("N_ijk! =", [math.factorial(i) for i in N_ijk], "=>", PT_j[parents_i_distinct_occurrences.index(j)])

    # here all the calculations
    result = 1
    for j in range(len(parents_i_distinct_occurrences)):  # the q_i loop
        tmp = factorial(len(node_i.var_domain) - 1) / factorial(N_ij[j] + len(node_i.var_domain) - 1)
        tmp *= PT_j[j]
        result *= tmp

    return result


def find_node_that_maximise_g(nodes_set: set, parents_set, cases_set):  # FIXME need testing
    # find node_z in nodes_set (i.e. 'nodes_array[i].parents - pi')
    # such that maximise g_function(node_z, pi+[node_z])

    max_g = 0
    max_g_node = 0
    for i in nodes_set:
        tmp_set = parents_set.copy()
        tmp_set.add(i)
        tmp = g_function(i, tmp_set, cases_set)
        if tmp > max_g:
            max_g = tmp
            max_g_node = i

    return max_g_node


def predecessors(node: Node, nodes_dict: dict, nodes_order) -> set:  # TODO

    pred = set()
    for i in nodes_order:
        if i != node.var_name:
            # print(i)
            pred.add(nodes_dict[i])
        else:
            break

    return pred


def k2_procedure(nodes_dict: dict, order_array, max_parents: int, cases_set) -> dict:  # FIXME need testing

    for node_name in nodes_dict:
        node = nodes_dict[node_name]
        print("k2 on node", node.var_name)
        pi = set()

        old_prob = g_function(node, pi, cases_set)

        should_exit = False
        while (not should_exit) and (len(pi) < max_parents):
            preds = predecessors(node, nodes_dict, order_array)
            node_z = find_node_that_maximise_g(preds - pi, pi, cases_set)  # TODO
            if node_z == 0:
                break

            tmp_parents = pi.union(node_z.parents)
            new_prob = g_function(node, tmp_parents , cases_set)
            if new_prob > old_prob:
                old_prob = new_prob
                pi.add(node_z)
            else:
                should_exit = True
        node.parents = pi  # "write node and its parents"

    return nodes_dict
