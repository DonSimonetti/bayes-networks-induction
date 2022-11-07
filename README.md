
# Apprendimento di rete bayesiana da un dataset
### Moduli
- [bayes_induction.py](https://github.com/DonSimonetti/bayes-networks-induction/blob/main/src/bayes_induction.py): è il modulo principale che lancia l'esecuzione dell'algoritmo K2 descritto nell'articolo di Cooper & Herskovits (1992). Deve ricevere come input la posizione del file CSV da cui leggere il dataset.

Esempio di riga di comando:
```
python bayes_induction.py file.csv
```
Per l'esecuzione si richiede la versione 3.8 di python con le seguenti dipendenze:
- pandas
- numpy
- graphviz
- pydot
