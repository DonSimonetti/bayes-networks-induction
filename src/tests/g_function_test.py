import bnlearn
import pandas

from src.gFunction import g_function
from src.node import Node


def test1():
    bn = bnlearn.import_DAG('alarm')
    samples = bnlearn.sampling(bn, 10)

    node_i = Node('CO', bn['model'].states['CO'])
    # parents = {'HISTORY', 'HYPOVOLEMIA'}
    parents = {}

    result = g_function(node_i, parents, samples)

    print("g_function result:", result)
    return


def test2():
    dataset_df = pandas.read_csv("../3000_samples_dataset.csv")
    node_i = Node("CATECHOL", [0, 1])
    r_i = len(node_i.var_domain)

    p_i = {"ARTCO2", "INSUFFANESTH"}
    #p_i = {}

    p_i_cases = dataset_df.filter(items=p_i).values.tolist()

    # calculate w_i and q_i by removing duplicates from p_i_cases
    w_i = list(set(tuple(i) for i in p_i_cases))
    q_i = len(w_i)

    # calculate N_i matrix
    columns = [node_i.var_name]
    columns.extend(p_i)
    pippo = dataset_df.filter(items=columns)

    N_i = [[0 for j in node_i.var_domain] for k in range(q_i)]

    for j in range(q_i):
        for k in node_i.var_domain:
            pluto = pippo.where(pippo[node_i.var_name] == k)
            if len(p_i) != 0:
                pluto.where(pippo[list(p_i)] == w_i[j], inplace=True)
            N_i[j][k] = pluto.dropna().count()[0]

    assert r_i == 2
    assert sum([sum(i) for i in N_i]) == 3000
    return


test2()
