import math
import numpy

import pandas

from src.node import Node


#  'node_i'     is a Node from node.py
#  'cases_df'   is a pandas DataFrame
def g_function(node_i: Node, parents: set, cases_df: pandas.DataFrame) -> float:  # TODO

    # calculate node_values_distribution
    node_values_distribution = [0 for i in node_i.var_domain]
    cases = cases_df[node_i.var_name].tolist()
    for value in cases:
        node_values_distribution[value] += 1  # this is the vector of the N_ij when the node has no parents

    # calculate r_i
    r_i = len(node_i.var_domain)

    # calculate w_ij and q_i
    w_i = []
    parents_cases = cases_df.filter(items=parents).values.tolist()
    for row in parents_cases:
        if row not in w_i:
            w_i.append(row)
    q_i = len(w_i)

    # calculate N_i matrix
    columns = [node_i.var_name]
    columns.extend(parents)
    pippo = cases_df.filter(items=columns)

    N_i = [[0 for j in w_i] for k in node_i.var_domain]
    for k in node_i.var_domain:
        for w_ij in w_i:
            pluto = pippo.where(pippo[node_i.var_name] == k)
            pluto.where(pippo[parents] == w_ij, inplace=True)
            pluto.dropna(inplace=True)
            N_i[k][w_i.index(w_ij)] = len(pluto.index)

                count[k] = pi_i_instances.count(pi)
            N_ij[parents_i_distinct_occurrences.index(pi)] = count

    # calculate N_ij
    # N_ij = sum(N_ij)
    return


        g_value *= (math.factorial(r_i-1)/math.factorial(N_ij + r_i - 1))*factorials_prod
    return g_value
