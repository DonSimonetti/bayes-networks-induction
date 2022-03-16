import bnlearn

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
parents_i_distinct_occurrences_count = []

node_i_name = 'CO'
node_i_possible_values = bn['model'].states[node_i_name]

filter_node = samples['CO'] == 0

print("v_i =", node_i_possible_values, "=> r_i =", len(node_i_possible_values))
print("pi_i =", parents_i_names)

for i in samples.filter(items=parents_i_names).values.tolist():
    if i not in parents_i_distinct_occurrences:
        parents_i_distinct_occurrences.append(i)
        parents_i_distinct_occurrences_count.append(1)
    else:
        parents_i_distinct_occurrences_count[parents_i_distinct_occurrences.index(i)] += 1

print("W_i =", parents_i_distinct_occurrences, "=> q_i =", len(parents_i_distinct_occurrences))

print("selecting the columns 'CO', 'HISTORY', 'HYPOVOLEMIA'")
for i in samples.filter(items=['CO', 'HISTORY', 'HYPOVOLEMIA']).values.tolist():
    print(i)

for k in node_i_possible_values:
    print("calculating N_ij set where 'CO' =", k, "(more precisely N_ijk where k = ", k, ")")
    N_ijk = []
    pippo = samples.filter(items=['HISTORY', 'HYPOVOLEMIA']).where(samples['CO'] == k).copy().dropna().values.tolist()

    for i in pippo:
        for j in range(len(i)):
            i[j] = int(i[j])

    print(pippo)
    for vec in parents_i_distinct_occurrences:
        print(pippo.count(vec))

# now for each possible k value of node_i calculate N_ijk, his factorial, and multiply them
