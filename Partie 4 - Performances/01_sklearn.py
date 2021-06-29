# Importation des librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Importation des données du casque
data = pd.read_excel('data.xlsx')
data.head()

# Parsing des données
y = data['Classe']
X = data.drop('Classe', axis=1)
# Creation du KNN
model = KNeighborsClassifier(3)
model.fit(X,y)
model.score(X,y)

# Donnée que l'on veut classer
x = np.array([329,415,243,153,393,317,260,123])
.reshape(1,8)

# Affichage de la prediction & probabilité
model.predict(x)
print(model.predict(x))
print(model.predict_proba(x))