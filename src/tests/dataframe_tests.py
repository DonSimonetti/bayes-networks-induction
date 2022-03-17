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

parents_i_names = ['HISTORY', 'HYPOVOLEMIA']
parents_i_distinct_occurrences = []

node_i_name = 'CO'
node_i_possible_values = bn['model'].states[node_i_name]

filter_node = samples[node_i_name] == 0

print("v_i =", node_i_possible_values, "=> r_i =", len(node_i_possible_values))
print("pi_i =", parents_i_names)

for i in samples.filter(items=parents_i_names).values.tolist():
    if i not in parents_i_distinct_occurrences:
        parents_i_distinct_occurrences.append(i)

print("W_i =", parents_i_distinct_occurrences, "=> q_i =", len(parents_i_distinct_occurrences))

print("selecting the columns", parents_i_names, ", ['"+node_i_name+"']")
for i in samples.filter(items=parents_i_names+[node_i_name]).values.tolist():
    print(i)

for j in parents_i_distinct_occurrences:
    print("for j =", j)
    N_ij = 0
    for k in node_i_possible_values:
        print("\tcalculating N_ij set where '"+node_i_name+"' =", k, "( more precisely N_ijk where k =", k, ")")
        pi_i_instances = samples.filter(items=parents_i_names) \
            .where(samples[node_i_name] == k).copy().dropna().values.tolist()

        # re-cast to int
        for i in pi_i_instances:
            for _j in range(len(i)):
                i[_j] = int(i[_j])
        #

        print("\t", pi_i_instances, "=>", pi_i_instances.count(j))
        N_ij += pi_i_instances.count(j)
    print("N_ij =", N_ij)

# now for each possible k value of node_i calculate N_ijk, his factorial, and multiply them
