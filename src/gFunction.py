import math
import numpy

import pandas

from src.node import Node
from math import factorial


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
    if len(parents) != 0:
        parents_cases = cases_df.filter(items=parents).values.tolist()
        for row in parents_cases:
            if row not in w_i:
                w_i.append(row)
    q_i = len(w_i)

    # calculate N_i matrix
    columns = [node_i.var_name]
    columns.extend(parents)
    pippo = cases_df.filter(items=columns)

    if q_i != 0:
        N_i = [[0 for j in w_i] for k in node_i.var_domain]
        for k in node_i.var_domain:
            pluto = pippo.where(pippo[node_i.var_name] == k)
            for w_ij in w_i:
                if q_i != 0:
                    pluto.where(pippo[parents] == w_ij, inplace=True)
                pluto.dropna(inplace=True)
                N_i[k][w_i.index(w_ij)] = len(pluto.index)
    else:
        N_i = []
        for k in node_i.var_domain:
            N_i.append([len(pippo.where(pippo[node_i.var_name] == k).dropna())])

    # calculate g_function value
    g_value = 1
    j = 0
    while j == 0 or j < q_i:
        N_ij = 0
        for i in range(r_i):
            N_ij += N_i[i][j]

        factorials_prod = 1
        for i in range(r_i):
            factorials_prod *= factorial(N_i[i][j])

        tmp1 = factorial(r_i - 1)
        tmp2 = factorial(N_ij + r_i - 1)
        g_value *= tmp1 * factorials_prod / tmp2
        j += 1
    return g_value
