import bnlearn
from src.gFunction import g_function
from src.node import Node

bn = bnlearn.import_DAG('../../alarm.bif')
samples = bnlearn.sampling(bn, 10)

node_i = Node('CO', bn['model'].states['CO'])
# parents = {'HISTORY', 'HYPOVOLEMIA'}
parents = {}

result = g_function(node_i, parents, samples)

print("g_function result:", result)
