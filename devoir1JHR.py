#coding: utf8

annee = [format(annee) for annee in range(30000, 100000)]

anne = ["{:05d}".format(anne) for anne in range(0, 18000)]

print(annee, anne)


# Cette solution fonctionne bien. Elle imprime successivement deux listes contenant tous les numéros de permis possibles dans l'intervalle qu'on cherche.
# Dans une perspective de journalisme de données, il est encore mieux de réunir l'ensemble de ces nombres dans une seule liste:

medecins = annee + anne

# Puis, de créer une boucle qui traite chacun des nombres (les numéros de permis possibles) un à un:

for medecin in medecins:
	print(medecin)