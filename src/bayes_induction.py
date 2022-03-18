import sys

import pandas
from K2 import k2_procedure

if len(sys.argv) != 2:
    print("SYNTAX ERROR: Usage: python bayes_induction.py [DATASET_CSV_FILE]", file=sys.stderr)
    exit(1)

dataset_df = pandas.read_csv(sys.argv[1])

# TODO read the dataframe and instantiate every node
# TODO put them in the 'nodes_array'
# TODO provide an 'order_array'
# TODO find appropriate 'max_parents'

# TODO run k2_procedure(nodes_array, order_array, max_parents, dataset_df)

# TODO build and plot the resulting DAG

