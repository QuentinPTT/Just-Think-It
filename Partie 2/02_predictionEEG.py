# Importation des librairies

from librairieKNN import KNN

# Importation de la classe
knn = KNN(3)

# Importer le dataset
data = knn.csv("data.csv")

# Supprimer le header & transformer les strings en int
del data[0]
data= [[int(float(j)) for j in i] for i in data]

# EX - Donnée d'entrainement
# 398,868,914,829,485,416,287,338,0
# 281,592,140,283,374,115,309,263,1
# 1164,294,234,419,295,337,379,365,2

# Nouveau point à classer
newPoint=[281,592,140,283,374,115,309,263]

# Prédiction du nouveau point
classe = knn.classification(data, newPoint)
prediction = classe[0]
print("La prédiction est", prediction)


