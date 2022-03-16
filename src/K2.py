from node import Node


def get_data_in_column(dataset, column):
    print("Selecting", column)
    result_list = []

    column_index = dataset[0].index(column)

    for i in range(1, len(dataset)):
        result_list.append(dataset[i][column_index])

    return result_list


def get_distinct_data_in_columns(dataset, columns):
    print("Selecting", columns)
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


def g_function(node, parents, case_set):  # TODO

    r_i = node.var_domain_size  # get the number of possible values for node (i.e. r_i)

    parents_instances = []  # I.E. the w_i, all the instances of 'parents' in the dataset
    parents_instances_size = 0  # I.E. the q_i
    if len(parents) == 0:
        # return algebraic multiplicity of its distribution image
        values_vec = get_data_in_column(case_set, node.var_name)
        return
    else:
        parents_instances = get_distinct_data_in_columns(case_set, parents)  # the w_i
        parents_instances_size = len(parents_instances)  # the q_i

    # here all the calculation
    result = 0.0
    for j in range(parents_instances_size):  # the q_i loop
        # TODO calculate result = (r_i - 1)!/(Nij + r_i - 1)!
        # for k in range(r_i):
        # TODO calculate result *= Nijk
        print(j)

    return result


def K2(nodes_array, order_array, max_parents, cases_database):  # TODO

    for i in order_array:
        node = nodes_array[order_array[i]]
        pi = []

        old_prob = g_function(node, pi, cases_database)

        should_exit = False
        while (not should_exit) and (len(pi) < max_parents):
            Z = Node()
            # TODO find node Z in 'nodes_array[i].parents \ pi' such that maximise g_function(Z,pi)

            new_prob = g_function(node, pi.copy().append(Z), cases_database)
            if new_prob > old_prob:
                old_prob = new_prob
                pi.append(Z)
            else:
                should_exit = True
        node.parents = pi  # "write node and its parents"

    return nodes_array
