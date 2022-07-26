import graphviz
import pydot

def display_graph():

    final_dag = graphviz.Source.from_file(filename="k2_mockup.gv", engine="neato")
    dag = pydot.graph_from_dot_data(final_dag.source)
    print(dag)

    final_dag.view()
    return


if __name__ == "__main__":
    display_graph()
