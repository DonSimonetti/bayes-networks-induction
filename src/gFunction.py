import math
import numpy

import pandas

from node import Node


#  'node_i'     is a Node from node.py
#  'cases_df'   is a pandas DataFrame
def g_function(node_i: Node, parents: set, cases_df: pandas.DataFrame) -> float:  # FIXME need testing

    # print("v_i =", node_i.var_domain, "=> r_i =", len(node_i.var_domain))
    # print("pi_i =", parents)

    is_parents_empty = len(parents) == 0

    if is_parents_empty:
        node_values_distribution = [0 for i in node_i.var_domain]
        cases = cases_df[node_i.var_name].tolist()
        for value in cases:
            node_values_distribution[value] += 1  # this is the vector of the N_ijk when the node has no parents

    parents_i_distinct_occurrences = []
    filtered_list = cases_df.filter(items=parents).values.tolist()
    for i in filtered_list:
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
        tmp1 = numpy.math.factorial(len(node_i.var_domain) - 1)
        tmp2 = numpy.math.factorial(N_ij[j] + len(node_i.var_domain) - 1)

        tmp = tmp1 * PT_j[j]
        tmp /= tmp2

        result *= tmp

    return result