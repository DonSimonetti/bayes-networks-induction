import bnlearn as bn
from pgmpy.models import BayesianNetwork
import graphviz
# Load asia DAG
model_true = bn.import_DAG('alarm')
# plot ground truth
G = bn.plot(model_true)

# Sampling
df = bn.sampling(model_true, n=10000)
# Structure learning of sampled dataset
model_learned = bn.structure_learning.fit(df, methodtype='hc', scoretype='k2')

# Plot based on structure learning of sampled data
bn.plot(model_learned)
# Compare networks and make plot
bn.compare_networks(model_true, model_learned, pos=G['pos'])

