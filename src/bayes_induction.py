import sys

import pandas
from node import Node
from K2 import k2_procedure

if len(sys.argv) != 2:
    print("SYNTAX ERROR: Usage: python bayes_induction.py [DATASET_CSV_FILE]", file=sys.stderr)
    exit(1)

dataset_df = pandas.read_csv(sys.argv[1])

# TODO read the dataframe and instantiate every node
nodes_array = []

for i in dataset_df.columns:
    # node = Node(i)

    tmp = dataset_df['ANAPHYLAXIS']
    print(tmp)

    # nodes_states_dict = bn['model'].states.copy()
    #
    # for i in nodes_states_dict:
    #     print(nodes_states_dict[i])

print(len(nodes_array))




# TODO put them in the 'nodes_array'
# TODO provide an 'order_array'
# TODO find appropriate 'max_parents'

# TODO run k2_procedure(nodes_array, order_array, max_parents, dataset_df)

# TODO build and plot the resulting DAG

