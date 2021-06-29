import matplotlib.pyplot as plt
## 7 Graphes du diaporama

x1,x2,x3=[1,2,0],[1.9,2.5,0],[1.4,1,0]
plt.xlim(0,3)
plt.ylim(0,3)
plt.scatter(x1[0],x1[1],color="green")
plt.scatter(x2[0],x2[1],color="green")
plt.scatter(x3[0],x3[1],color="red")
plt.savefig('1.pdf')

x1,x2,x3=[1,2,0],[1.9,2.5,0],[1.4,1,0]
newPoint=[1.5,1.5,0]
plt.xlim(0,3)
plt.ylim(0,3)
plt.scatter(x1[0],x1[1],color="green")
plt.scatter(x2[0],x2[1],color="green")
plt.scatter(x3[0],x3[1],color="red")
plt.scatter(newPoint[0],newPoint[1],color="blue")
plt.savefig('2.pdf')

x1,x2,x3=[1,2,0],[1.9,2.5,0],[1.4,1,0]
newPoint=[1.5,1.5,0]
plt.xlim(0,3)
plt.ylim(0,3)
plt.scatter(x1[0],x1[1],color="green")
plt.scatter(x2[0],x2[1],color="green")
plt.scatter(x3[0],x3[1],color="red")
plt.scatter(newPoint[0],newPoint[1],color="blue")
plt.plot([x1[0],newPoint[0]],[x1[1],newPoint[1]],color="blue")
plt.savefig('3.pdf')

x1,x2,x3=[1,2,0],[1.9,2.5,0],[1.4,1,0]
newPoint=[1.5,1.5,0]
plt.xlim(0,3)
plt.ylim(0,3)
plt.scatter(x1[0],x1[1],color="green")
plt.scatter(x2[0],x2[1],color="green")
plt.scatter(x3[0],x3[1],color="red")
plt.scatter(newPoint[0],newPoint[1],color="blue")
plt.plot([x1[0],newPoint[0]],[x1[1],newPoint[1]],color="blue")
plt.plot([x2[0],newPoint[0]],[x2[1],newPoint[1]],color="blue")
plt.savefig('4.pdf')

x1,x2,x3=[1,2,0],[1.9,2.5,0],[1.4,1,0]
newPoint=[1.5,1.5,0]
plt.xlim(0,3)
plt.ylim(0,3)
plt.scatter(x1[0],x1[1],color="green")
plt.scatter(x2[0],x2[1],color="green")
plt.scatter(x3[0],x3[1],color="red")
plt.scatter(newPoint[0],newPoint[1],color="blue")
plt.plot([x1[0],newPoint[0]],[x1[1],newPoint[1]],color="blue")
plt.plot([x2[0],newPoint[0]],[x2[1],newPoint[1]],color="blue")
plt.plot([x3[0],newPoint[0]],[x3[1],newPoint[1]],color="blue")
plt.savefig('5.pdf')

x1,x2,x3=[1,2,0],[1.9,2.5,0],[1.4,1,0]
newPoint=[1.5,1.5,0]
plt.xlim(0,3)
plt.ylim(0,3)
plt.scatter(x1[0],x1[1],color="green")
plt.scatter(x2[0],x2[1],color="green")
plt.scatter(x3[0],x3[1],color="red")
plt.scatter(newPoint[0],newPoint[1],color="blue")
plt.plot([x1[0],newPoint[0]],[x1[1],newPoint[1]],color="gray")
plt.plot([x2[0],newPoint[0]],[x2[1],newPoint[1]],color="gray")
plt.plot([x3[0],newPoint[0]],[x3[1],newPoint[1]],color="blue")
plt.savefig('6.pdf')

x1,x2,x3=[1,2,0],[1.9,2.5,0],[1.4,1,0]
newPoint=[1.5,1.5,0]
plt.xlim(0,3)
plt.ylim(0,3)
plt.scatter(x1[0],x1[1],color="green")
plt.scatter(x2[0],x2[1],color="green")
plt.scatter(x3[0],x3[1],color="red")
plt.scatter(newPoint[0],newPoint[1],color="red")
plt.savefig('7.pdf')