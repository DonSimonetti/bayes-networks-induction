import sys

import bnlearn

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
filename = samples_count.__str__()+"_samples_dataset"
samples.to_csv(filename+".csv", index=False)

