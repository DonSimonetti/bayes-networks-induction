import bnlearn

bn = bnlearn.import_DAG('../alarm.bif')
samples = bnlearn.sampling(bn, 100)

samples_list = samples.values.tolist()
print(samples.columns)
for i in samples.columns:
    print(i)
print(len(samples.columns))
