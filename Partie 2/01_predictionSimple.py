# Importation des librairies

import numpy as np
import matplotlib.pyplot as plt
from librairieKNN import KNN

# Dataset d'entrainement
data = [[3.308385527027144,2.550537003,0],
[2.6775807924251267,3.9862474547518043,0],
[4.665561423800724,0.060155338394774494,0],
[3.7987537802580706,0.04582398699792334,0],
[2.9415460956523782,0.89728186192509955,0],
[1.1838870544929065,3.960698192743375,1],
[1.090381001867262,0.9469091818299019,1],
[0.13860555788758133,4.750241628618403,1],
[1.464404890279014,6.448155413578278,1],
[2.095287604176638,0.23873771010436984,1]]

# Séparation du dataset
array=np.array(data)
X1=array[:,0]
X2=array[:,1]
Y=array[:,2]

# Importation de la classe
knn = KNN(2)

# Prédiction d'un nouveau point
newPoint = [2,4,0]
classe = knn.classification(data, newPoint)
prediction = classe[0]
print("Notre prédiction est: " + str(prediction))

# Calcul de la distance euclidienne entre le newPoint et le dernier voisin
xV,yV = classe[1], classe[2]
distance = knn.distance_euclidienne(newPoint,[xV,yV])

# Création du graphe
plt.figure(figsize=(6,6))
plt.xlim(-1,6)
plt.ylim(-1,6)
plt.scatter(X1[0:5],X2[0:5],c='green',marker='x', label="Classe 0")
plt.scatter(X1[5:10],X2[5:10],c='red',marker='x',label="Classe 1")
plt.scatter(newPoint[0],newPoint[1],c="blue")

# Création du cercle de rayon de la distance euclidienne
circle = plt.Circle((newPoint[0],newPoint[1]), distance, fill=False,color='blue')
plt.gca().add_patch(circle)

# Affichage du graphe
plt.legend()
plt.show()