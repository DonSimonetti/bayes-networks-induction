import torch
import bnlearn

bn = bnlearn.import_DAG('../alarm.bif')
samples = bnlearn.sampling(bn, 1000)
