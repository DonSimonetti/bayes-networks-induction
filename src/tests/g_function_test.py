import bnlearn
from src.K2 import g_function
from src.node import Node

bn = bnlearn.import_DAG('../../alarm.bif')
samples = bnlearn.sampling(bn, 10)

node_i = Node()
node_i.var_name = 'CO'
node_i.var_domain = bn['model'].states[node_i.var_name]
parents = {'HISTORY', 'HYPOVOLEMIA'}

result = g_function(node_i, parents, samples)

print("g_function result:", result)
