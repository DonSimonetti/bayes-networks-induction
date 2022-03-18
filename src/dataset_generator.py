import sys

import bnlearn
import pickle
from pandas import DataFrame

if len(sys.argv) != 2:
    print("SYNTAX ERROR: Usage: python dataset_generator.py [NUMBER OF SAMPLES]", file=sys.stderr)
    exit(1)

if not sys.argv[1].isnumeric():
    print("SYNTAX ERROR: Usage: python dataset_generator.py [NUMBER OF SAMPLES]", file=sys.stderr)
    exit(1)

samples_count = int(sys.argv[1])
print("Generating", samples_count, "samples with bnlearn")

bn = bnlearn.import_DAG('../alarm.bif')
samples = bnlearn.sampling(bn, samples_count)
# samples_list = samples.values.tolist()
#
# print("Dumping the samples with pickle..")
# samples_list = [samples.columns.tolist()] + samples_list
# for i in samples_list:
#     print(i)
#
# serialized_sample_list = pickle.dumps(samples_list)
filename = samples_count.__str__()+"_samples_dataset"
# filename += ".obj"
# dataset_file = open(filename, "wb")
# dataset_file.write(serialized_sample_list)
# dataset_file.close()

# print(samples_list[0].index('BP'))
# print(serialized_sample_list)
# print(samples.columns.tolist())

samples.to_csv(filename+".csv")

