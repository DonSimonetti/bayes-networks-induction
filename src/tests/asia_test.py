import bnlearn as bn
from pgmpy.models import BayesianNetwork
import graphviz
# Load asia DAG
model_true = bn.import_DAG('asia')
# plot ground truth
graph = model_true["model"]
graph.plot()

# Sampling
df = bn.sampling(model_true, n=10000)
# Structure learning of sampled dataset
model_learned = bn.structure_learning.fit(df, methodtype='hc', scoretype='bic')

# Plot based on structure learning of sampled data
#bn.plot(model_learned, pos=G['pos'], interactive=True)
# Compare networks and make plot
#bn.compare_networks(model_true, model_learned, pos=G['pos'])

