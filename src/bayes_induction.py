import sys

import pandas
import pickle
from node import Node
from K2 import k2_procedure
from graphviz import Digraph

if len(sys.argv) != 2:
    print("SYNTAX ERROR: Usage: python bayes_induction.py [DATASET_CSV_FILE]", file=sys.stderr)
    exit(1)

dataset_df = pandas.read_csv(sys.argv[1])

# read the dataframe, instantiate every node and put them in 'nodes_array'
nodes_dict = {}
vars_file = open("variables_constraints.obj", "rb")
vars_constraints = pickle.load(vars_file)
vars_file.close()

for i in dataset_df.columns:
    to_numbers = [vars_constraints[i].index(j) for j in vars_constraints[i]]
    node = Node(i, to_numbers)
    nodes_dict[i] = node

assert len(nodes_dict) == 37

# provide an 'order_array'
# i'll take the order given by 'dataset_df'
order_array = [list(nodes_dict.keys())[i] for i in range(0, len(nodes_dict))]

# find appropriate 'max_parents'
# reading from 'https://www.bnlearn.com/bnrepository/discrete-medium.html'
# we can see that the maximum in-degree of the target network is 4. So..
max_parents = 4

# FIXME run k2_procedure(nodes_dict, order_array, max_parents, dataset_df)
# new_nodes_dict = k2_procedure(nodes_dict, order_array, max_parents, dataset_df)

# TODO build and plot the resulting DAG
final_dag = Digraph()
for node in nodes_dict:
    final_dag.node(node)
    final_dag.edge(node,'BP')


final_dag.render(view=True)
