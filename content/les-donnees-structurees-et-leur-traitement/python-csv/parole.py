import pandas
parole = pandas.read_csv("20190308-years.csv")

for année in  (1999, 2009, 2019):
    print(année, parole.loc[(parole['year'] == année), ["channel_name", "women_expression_rate"]].mean())
    
recherche = parole.loc[(parole['year'] == 2019), ["channel_name", "women_expression_rate"]]
tri = recherche.sort_values(by="women_expression_rate")
print(tri)
