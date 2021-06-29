def csv(self, nom):
    dataset = list()
    with open(nom, 'r') as fichier:
        csv_reader = reader(fichier)
        for l in csv_reader:
            if not l:
                continue
            dataset.append(l)
    return dataset