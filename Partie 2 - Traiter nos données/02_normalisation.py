def minMax(dataset):
    minmax = []
    for i in range(len(dataset[0])-1):
        col = [l[i] for l in dataset]
        vMin = min(col)
        vMax = max(col)
        minmax.append([vMin, vMax])
    return minmax

def normaliser(dataset, minmax):
    lNormalise = dataset.copy()
    for k in range (len(dataset)):
        for i in range (len(dataset[k])-1):
            lNormalise[k][i] = (dataset[k][i] - 
            minmax[i][0])/(minmax[i][1] - minmax[i][0])
    return lNormalise