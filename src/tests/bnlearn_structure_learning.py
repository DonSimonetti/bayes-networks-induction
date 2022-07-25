import bnlearn as bn

true_model = bn.import_DAG("asia")

dataset = bn.sampling(true_model, 10000)
learned_model = bn.structure_learning.fit(dataset, scoretype='k2')

G = bn.plot(true_model)
bn.plot(learned_model, pos=G['pos'])
bn.compare_networks(true_model, learned_model, pos=G['pos'])
