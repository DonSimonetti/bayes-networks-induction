
# Apprendimento di rete bayesiana da un dataset
### Moduli
- [bayes_induction.py](src/bayes_induction.py): è il modulo principale che lancia l'esecuzione di K2 (Cooper & Herskovits, 1992) e renderizza il risultato nel file *k2_result_N.svg* dove 'N' è la grandezza del dataset. Deve ricevere come input la posizione del file CSV da cui leggere il dataset.

  Esempio di riga di comando:
  ```
  python bayes_induction.py file.csv
  ```
  Per l'esecuzione si richiede la versione 3.8 di python con le seguenti dipendenze:
  - pandas
  - numpy
  - graphviz
  - pydot

- [dataset_generator.py](src/dataset_generator.py): questo è uno script che genera un dataset di grandezza arbitraria in formato CSV. Per eseguirlo bisogna che il pacchetto *bnlearn* sia installato (vedi [qui](https://pypi.org/project/bnlearn/)).
  Esempio:
  ```
  python dataset_generator.py 3000
  ```
- [K2.py](src/K2.py): modulo python che fornisce l'implementazione dell'algoritmo K2.
- [gFunction.py](src/gFunction.py): modulo python che fornisce l'implementazione della funzione 12 dell'articolo ![equation](https://latex.codecogs.com/svg.image?g(i,&space;\pi_{i})).
- [node.py](src/node.py): fornisce una implementazione molto basilare della classe nodo.
- [global_vars.py](src/global_vars.py): contiene due ordinamenti possibili utilizzati da ```K2.k2_procedure()```.
- [variables_constraint_parser.py](src/variables_constraint_parser.py): contiene la funzione che estrapola il dominio dei valori di ogni variabile dal file   *alarm_variables_constraints.txt*

Per semplificare il tutto ho anche inserito lo script bash ```run_all_datasets.sh``` che esegue K2 su datasets di grandezze diverse predefinite.
