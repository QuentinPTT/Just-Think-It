from math import *
from csv import reader

class KNN:
    """
    Librairie KNN
    """

    def __init__(self, k):
        self.k = k
        
    """
    Importer des données sous .csv
    """
    def csv(self, filename):
        dataset = list()
        with open(filename, 'r') as file:
            csv_reader = reader(file)
            for row in csv_reader:
                if not row:
                    continue
                dataset.append(row)
        return dataset

    """ 
    Calculer la distance euclidienne pour n dimension de l2 par rapport à l1
    """
    def distance_euclidienne(self, l1, l2):
        # Initilisation de la ditance
        distance = 0
        # l2 contient les coordonnées du point à n dimension
        # On calcule la distance euclidienne à n dimension avec la formule
        for k in range(len(l1)-1):
            distance += (l1[k] - l2[k])**2
        return sqrt(distance)

    """ 
    Localiser les voisins les plus proches
    """
    def procheVoisins(self, train, testL):
        # Initialisation de la distance qui contiendra après la boucle, les distances euclidiennes de trainL par rapport à testL
        distances = []
        for trainL in train:
            distance = self.distance_euclidienne(testL, trainL)
            distances.append([trainL, distance])
        # On tri la liste dans l'ordre croissant par rapport au deuxième élément de la liste ex:
        # [(5,6),(2,3),(5,5)] devient [(2, 3), (5, 5), (5, 6)]
        distances.sort(key=lambda lis: lis[1])
        voisins = []
        # On stocke pour k voisins, la classe du plus petit k correspondant dans la liste distances
        for i in range(self.k):
            voisins.append(distances[i][0])
        return voisins

    """
    Produire une prédiction en déterminer la classe
    """
    def classification(self, train, testL):
        # On récupére l
        voisins = self.procheVoisins(train, testL)
        sortie = [l[-1] for l in voisins]
        prediction = max(sortie, key=sortie.count)
        return prediction,voisins[-1][0], voisins[-1][1]

