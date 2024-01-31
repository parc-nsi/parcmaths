# -*- coding: utf-8 -*-

# Etape 1
# D'après la première information Sophie est sure d'avoir la somme donc 
# On sait que Sophie a tiré un nombre premier entre 4 et 40 
# Pour toutes les décompositions en somme x + y des premiers entre 4 et 40
# on calcule le produit et on associe dans un dictionnaire  germain à ce produit x * y
# la liste des décompositions  (x, y)

germain = dict()
for s in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:    
    for x in range(max(2, s - 20), s // 2 + 1):
        p = x * (s -x)
        if p not in germain:
            germain[p] = [(x, s -x)]
        else:
            germain[p].append((x, s -x))
            
# Etape 2
# D'après la seconde information Germain a compris que la somme détenue par Sophie 
# est un nombre premier mais pour le produit x * y il existe plusieurs décompositions 
# en somme x + y avec x + y premiers
# On filtre donc dans le dictionnaaire germain les clefs = produit x * y
# telles que x * y a plus d'une décompsoition avec x + y premier
# c'est-à-dire que  len(germain[(x, y)]) >= 2
# on sélectionne :
#            30: [(5, 6), (3, 10), (2, 15)]
#            42: [(6, 7), (3, 14)]
#             60: [(5, 12), (4, 15), (3, 20)]
#              70: [(7, 10), (5, 14)]
#               90: [(9, 10), (5, 18)]
# Ce sont les solutions possibles du point de vue de Germain
            
# Etape 3 : Sophie déclare alors qu'elle connait la solution
# C'est-à-dire que dans les décompositions en omme x + y de son nombre 
# une seule est telle que x * y est associéé à plusieurs décompositions dans le 
# dictionnaire germain
            
# Pouir trouver le nombre de Sophie on peut "inverser" ce qu'il reste dans le 
# dictionnaire de Germain après le filtrage précédent
# On associe chaque couple (x, y) possible
# c'est-à-dire (5, 6), (3, 10), (2, 15), (6, 7), (3, 14), (5, 12), (4, 15), (3, 20), (7, 10), (5, 14), (9, 10), (5, 18)
# comme solution possible associée à la somme x + y (qui serait le nombre détenu par Sophie)
# On obtient :
#{11: [(5, 6)],
# 13: [(3, 10), (6, 7)],
# 17: [(2, 15), (3, 14), (5, 12), (7, 10)],
# 19: [(4, 15), (5, 14), (9, 10)],
# 23: [(3, 20), (5, 18)]}
# Ce sont les solutions possibles du point de vue de Sophie
# Le nombre de Sophie est 11 car c'est le seul qui correspond à une seule solution possible pour Germain
# Et Sophie a bien dit qu'elle avait la solution

# Etape 4 : Germain est informé que Sophie a la solution donc il peut raisonner comme elle pour la trouver
            
# COnclusion : Sophie a le nombre 11 et Germain le 30 et les enfants du professeur ont 5 et 6 ans 

sophie = dict()
for p in germain:
    
    if len(germain[p]) >= 2:
        for (x, y) in germain[p]:
            s = x + y
            if s not in sophie:
                sophie[s] = [(x, y)]
            else:
                sophie[s].append((x, y))
print("Solution = ", {s : sophie[s] for s in sophie if len(sophie[s]) == 1})
