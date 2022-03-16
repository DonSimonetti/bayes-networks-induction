import bnlearn

bn = bnlearn.import_DAG('../../alarm.bif')
samples = bnlearn.sampling(bn, 10)

for i in samples.filter(items=['CO', 'BP', 'VENTALV']).values.tolist():
    print(i)

# this is how to get the values below used to calculate Nijk
distinct_occurrences = []
distinct_occurrences_count = []

for i in samples.filter(items=['CO', 'BP', 'VENTALV']).values.tolist():
    if i not in distinct_occurrences:
        distinct_occurrences.append(i)
        distinct_occurrences_count.append(1)
    else:
        distinct_occurrences_count[distinct_occurrences.index(i)] += 1

print(" --- ")
print(distinct_occurrences)
print(" --- ")
print(distinct_occurrences_count)

# how to filter
print("filtering")
filter1 = samples['CO'] == 0
filter2 = samples['BP'] == 0

print(samples.filter(items=['CO', 'BP', 'VENTALV']).where(filter1 | filter2).dropna())

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
