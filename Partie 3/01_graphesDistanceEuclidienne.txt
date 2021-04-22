import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

## Graphes en 2 dimensions

# Graphe avec les points
x,y=[2,4],[3,1]
plt.xlim(0,6)
plt.ylim(0,4)
plt.scatter(x,y,color='blue')
plt.text(1.95,2.6,'A')
plt.text(3.95,0.6,'B')
plt.savefig('graphe2DPoints.pdf')

# Graphe avec la distance
x,y=[2,4],[3,1]
plt.xlim(0,6)
plt.ylim(0,4)
plt.scatter(x,y)
plt.plot(x,y,color='green')
plt.text(1.8,1.7, "Distance-> d")
plt.text(1.95,2.6,'A')
plt.text(3.95,0.6,'B')
plt.savefig('graphe2DDistance.pdf')

## Graphes en 3 dimensions

# Graphe avec les points
x,y,z=[2,4],[3,1],[2,3]
fig = plt.figure()
ax = fig.gca(projection='3d')  # Affichage en 3D
ax.scatter(x, y, z, label='Courbe', marker='d')  # Tracé des points 3D
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.savefig('graphe3DPoints.pdf')

# Graphe avec la distance
x,y,z=[2,4],[3,1],[2,3]
fig = plt.figure()
ax = fig.gca(projection='3d')  # Affichage en 3D
ax.scatter(x, y, z, label='Courbe', marker='d',color='blue')
ax.plot(x, y, z, label='Courbe', marker='d',color='green')  # Tracé des points 3D
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.savefig('graphe3DDistance.pdf')
