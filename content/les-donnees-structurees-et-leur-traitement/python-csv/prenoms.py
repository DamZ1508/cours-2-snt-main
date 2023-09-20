import pandas

année = input("Année ? ")
if not année:
    année = "2021"
    
département = input("Département ? ")
if not département:
    département = "38"
    
prénoms = input("Prénom ? ").split()

data = pandas.read_csv("dpt2021.csv", sep=";")

print(data.loc[(data['dpt'] == département) & (data['annais'] == année), :].sort_values(by="nombre"))
for prénom in prénoms:
    print(data.loc[(data['dpt'] == département) & (data['annais'] == année) & (data['preusuel'] == prénom.upper()), :])
