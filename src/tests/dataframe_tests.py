import math

import bnlearn
from src import node

bn = bnlearn.import_DAG('../../alarm.bif')
samples = bnlearn.sampling(bn, 10)

# for i in samples.filter(items=['CO', 'BP', 'VENTALV']).values.tolist():
#     print(i)

# this is how to get the values below used to calculate Nijk
# distinct_occurrences = []
# distinct_occurrences_count = []
#
# for i in samples.filter(items=['CO', 'BP', 'VENTALV']).values.tolist():
#     if i not in distinct_occurrences:
#         distinct_occurrences.append(i)
#         distinct_occurrences_count.append(1)
#     else:
#         distinct_occurrences_count[distinct_occurrences.index(i)] += 1
#
# print(" --- ")
# print(distinct_occurrences)
# print(" --- ")
# print(distinct_occurrences_count)

# how to filter
# print("filtering")
# filter1 = samples['CO'] == 0
# filter2 = samples['BP'] == 0
#
# print(samples.filter(items=['CO', 'BP', 'VENTALV']).where(filter1 | filter2).dropna())

# this is how to select some columns
# for i in samples.filter(items=['CO', 'BP']).values.tolist():
#     print(i)


# this is how to get all the possible states of a node

# print(bn['model'].states['VENTALV'])
#
# nodes_states_dict = bn['model'].states.copy()
#
# for i in nodes_states_dict:
#     print(nodes_states_dict[i])


# putting all together..

print("putting all together..")

node_i = node.Node('CO', bn['model'].states['CO'])
parents = ['HISTORY', 'HYPOVOLEMIA']
parents_i_distinct_occurrences = []

print("v_i =", node_i.var_domain, "=> r_i =", len(node_i.var_domain))
print("pi_i =", parents)

print("selecting the columns", parents, ", ['" + node_i.var_name + "']")
for i in samples.filter(items=parents + [node_i.var_name]).values.tolist():
    print(i)

for i in samples.filter(items=parents).values.tolist():
    if i not in parents_i_distinct_occurrences:
        parents_i_distinct_occurrences.append(i)

print("W_i =", parents_i_distinct_occurrences, "=> q_i =", len(parents_i_distinct_occurrences))

for j in parents_i_distinct_occurrences:
    print("for j =", j)
    N_ijk = []
    for k in node_i.var_domain:
        print("\tcalculating N_ij set where '" + node_i.var_name + "' =", k, "( more precisely N_ijk where k =", k, ")")
        pi_i_instances = samples.filter(items=parents) \
            .where(samples[node_i.var_name] == k).copy().dropna().values.tolist()

        # re-cast to int
        for i in pi_i_instances:
            for _j in range(len(i)):
                i[_j] = int(i[_j])
        #

        print("\t", pi_i_instances)
        N_ijk.append(pi_i_instances.count(j))

    # now we have N_ijk for each possible k value of node_i
    # now calculate their factorials, and multiply them
    print("N_ijk =", N_ijk, "=> N_ij =", sum(N_ijk))
    print("N_ijk! =", [math.factorial(i) for i in N_ijk], "=>", math.prod([math.factorial(i) for i in N_ijk]))
