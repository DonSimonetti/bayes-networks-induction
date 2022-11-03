import decimal
from decimal import Decimal

import pandas

from src.node import Node
from math import factorial


#  'node_i'     is a Node from node.py
#  'parents'    is a set of variables' names (basically strings)
#  'cases_df'   is a pandas DataFrame
def g_function(node_i: Node, p_i: set, cases_df: pandas.DataFrame) -> Decimal:

    # calculate r_i
    r_i = len(node_i.var_domain)

    # calculate w_i and q_i by removing duplicates from p_i cases
    if len(p_i) == 0:
        w_i = [[]]
    else:
        w_i = cases_df.filter(items=p_i).drop_duplicates(ignore_index=True).values.tolist()
    q_i = len(w_i)

    # calculate N_i matrix
    columns = [node_i.var_name]
    columns.extend(p_i)
    temp = cases_df.filter(items=columns)

    N_i = [[0 for j in node_i.var_domain] for k in range(q_i)]

    for j in range(q_i):
        for k in node_i.var_domain:
            pluto = temp.where(temp[node_i.var_name] == k)
            if len(p_i) != 0:
                pluto.where(temp[list(p_i)] == w_i[j], inplace=True)
            N_i[j][k] = pluto.dropna().count()[0]

    # The code above is "correct" (tested many times)

    # calculate g_function value
    g_value = decimal.Decimal(1)
    for j in range(q_i):
        N_ij = sum(N_i[j])

        factorials_prod = decimal.Decimal(1)
        for i in range(r_i):
            factorials_prod *= factorial(N_i[j][i])

        tmp1 = decimal.Decimal(factorial(r_i - 1))
        tmp2 = decimal.Decimal(factorial(N_ij + r_i - 1))
        tmp3 = factorials_prod / tmp2
        g_value *= tmp1 * tmp3
    return g_value
