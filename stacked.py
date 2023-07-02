import matplotlib.pyplot as plt

# initialize variables

montants_Aeroport, montants_autre = 0, 0

# Read data from CSV file
with open("result.txt") as fichier:
    for ligne in fichier:
        # Split the line into a list of values
        valeurs = ligne.split(",")
        gare = valeurs[0]
        montant = int(valeurs[-1])
        
        if "AEROPORT CHARLES DE GAULLE" in gare:
            montants_Aeroport += montant
        else:
            montants_autre += montant

# Create the stacked bar chart
fig, ax = plt.subplots()

values = [montants_Aeroport, montants_autre]
pourcent = (montants_Aeroport/(montants_Aeroport+montants_autre)*100).__str__()
pourcent = round(float(pourcent), 2)

plt.xlabel('Proportion aéroport/total : ' + pourcent.__str__() + '%')

ax.bar("Voyageurs", montants_Aeroport, 0.6, label="Aeroport", bottom=0)
ax.bar("Voyageurs", montants_autre, 0.6, label="Autres", bottom=montants_Aeroport)

# Add labels on the center of the bars
ax.text("Voyageurs", montants_Aeroport/2, str(montants_Aeroport), ha='center', va='bottom')
ax.text("Voyageurs", montants_Aeroport + montants_autre/2, str(montants_autre), ha='center', va='bottom')


ax.set_title("Nombre de voyageurs en destination de CDG par rapport au reste du trafic")
ax.legend(loc="upper right")
plt.show()