import bnlearn
from src.K2 import g_function
from src.node import Node

bn = bnlearn.import_DAG('../../alarm.bif')
samples = bnlearn.sampling(bn, 10)

node_i = Node()
node_i.var_name = 'CO'
node_i.var_domain = bn['model'].states[node_i.var_name]
node_i.var_domain_size = len(node_i.var_domain)  # maybe this is useless. I'll remove it when I'll be sure
parents = ['HISTORY', 'HYPOVOLEMIA']

result = g_function(node_i, parents, samples)

print(result)
