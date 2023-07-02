import matplotlib.pyplot as plt

montants_par_ligne = {}

with open("result.txt") as fichier:
    for ligne in fichier:
        valeurs = ligne.split(",")
        currentLigne = valeurs[3]
        montant = int(valeurs[-1])
        
        # Add the amount to the total for the current line
        if currentLigne in montants_par_ligne:
            montants_par_ligne[currentLigne] += montant
        else:
            montants_par_ligne[currentLigne] = montant

# Sorting the lines by amount of passengers
lignes = sorted(montants_par_ligne, key=montants_par_ligne.get, reverse=True)

# Create lists of names and amounts for the graph
noms = []
montants = []
for current in lignes:
    noms.append(current)
    montants.append(montants_par_ligne[current])

# Create the bar chart
fig, ax = plt.subplots()
ax.barh(noms, montants)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("Voyageurs")
ax.set_ylabel("Lignes")
ax.set_title("Nombre de voyageurs par ligne")

plt.show()