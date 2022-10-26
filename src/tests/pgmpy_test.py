import matplotlib.pyplot as plt
from pgmpy.utils import get_example_model
import networkx as nx

alarm = get_example_model("alarm")
digraph = alarm.adj
G = nx.DiGraph()

nx.draw_networkx(alarm)
plt.show()
