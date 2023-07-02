import matplotlib.pyplot as plt

montants_par_ligne = {}

with open("result.txt") as fichier:
    for ligne in fichier:
        valeurs = ligne.split(",")
        currentLigne = valeurs[3]
        montant = int(valeurs[-1])
        
        # Ajouter le montant à la somme pour cette gare dans le dictionnaire
        if currentLigne in montants_par_ligne:
            montants_par_ligne[currentLigne] += montant
        else:
            montants_par_ligne[currentLigne] = montant

# Trier les gares par ordre décroissant de montants
lignes = sorted(montants_par_ligne, key=montants_par_ligne.get, reverse=True)

# Créer les listes de noms de gares et de montants correspondants pour le graphique
noms = []
montants = []
for current in lignes:
    noms.append(current)
    montants.append(montants_par_ligne[current])

# Créer le graphique à barres horizontales
fig, ax = plt.subplots()
ax.barh(noms, montants)
ax.invert_yaxis()  # Inverser l'ordre des gares pour que les plus grandes soient en haut
ax.set_xlabel("Voyageurs")
ax.set_ylabel("Lignes")
ax.set_title("Nombre de voyageurs par ligne")

plt.show()