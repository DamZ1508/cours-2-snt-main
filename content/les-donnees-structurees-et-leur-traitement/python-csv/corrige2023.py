import pandas
prenoms = pandas.read_csv("dpt2021.csv", sep=";")
recherche = prenoms.loc[:, "preusuel"]
print(recherche)
