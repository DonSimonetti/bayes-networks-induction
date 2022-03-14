import pickle


def get_distinct_data_in_columns(dataset, columns):
    print("Selecting",columns)
    result_list = []

    columns_indexes = []
    for column in columns:
        columns_indexes.append(dataset[0].index(column))

    # print(columns_indexes)

    for i in range(1, len(dataset)):
        vec = []
        for index in columns_indexes:
            vec.append(dataset[i][index])
        if vec not in result_list:
            result_list.append(vec)

    return result_list


_dataset = open("10_samples_dataset.obj", "rb")
serialized_str = _dataset.read()
_dataset.close()
deserialized_set = pickle.loads(serialized_str)
#for i in deserialized_set:
    #print(i)

_columns = get_distinct_data_in_columns(deserialized_set, ['HISTORY', 'CVP', 'PCWP', 'BP'])


#print(_columns)
for j in _columns:
    print(j)

