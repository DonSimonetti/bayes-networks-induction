import sys

import graphviz
import pandas
import pickle
import pydot
from node import Node
from K2 import k2_procedure

if len(sys.argv) != 2:
    print("SYNTAX ERROR: Usage: python bayes_induction.py [DATASET_CSV_FILE]", file=sys.stderr)
    exit(1)

dataset_df = pandas.read_csv(sys.argv[1])

# read the dataframe, instantiate every node and put them in 'nodes_dict'
nodes_dict = {}
vars_file = open("variables_constraints.obj", "rb")
vars_domains = pickle.load(vars_file)
vars_file.close()

for i in dataset_df.columns:
    to_numbers = [vars_domains[i].index(j) for j in vars_domains[i]]
    node = Node(i, to_numbers)
    nodes_dict[i] = node

assert len(nodes_dict) == 37

# provide an 'order_array'
# I'll take the order I manually generated
from global_vars import order_array

# find appropriate 'max_parents'
# reading from 'https://www.bnlearn.com/bnrepository/discrete-medium.html'
# we can see that the maximum in-degree of the target network is 4. So..
max_parents = 4

# FIXME resulting DAG is not even close to the original
new_nodes_dict = k2_procedure(nodes_dict, order_array, max_parents, dataset_df)

dag_sources = graphviz.Source.from_file(filename="k2_mockup.gv", engine="neato").source
resulting_graph = pydot.graph_from_dot_data(dag_sources)[0]

for node in new_nodes_dict:
    for parent in nodes_dict[node].parents:
        edge = pydot.Edge(parent, node)
        resulting_graph.add_edge(edge)

resulting_graph.write("k2_result.pdf", format='pdf', prog='neato')
