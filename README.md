# Analyse du dataset du Titanic avec python

1. On importe nos modules nécessaires pour l'analyse

numpy,panda,matplotlib.pyplot

2. On importe notre dataset avec pandas

pd.read_excel('titanic_data.xls')

3. On élémine les données qu’on n’a pas besoin 

qui veut dire suprimer quelque colones avec la fonctions drop() selon l'axis =1

4. Faire une petite analyse des ensembles de nos données

avec la fonction describe() on peut avoir le min le max la moayenne ....

5. Sur notre dataFrame il manque quelque donnée d’Age

alors grace a la fonction dropna() on supprimes toute les ligne ou l'age n'est pas mentionné

6. Voila on est avec un dataFrame complet on peut commencer

7. Afficher le nombre de personne de chaque classe sur le bateau

avec la fonction value_counts()

8. Avec pyplot on affiche un petit graphe de cette selection de données

9. Regrouper l'ensemble des voyageurs selon leur sexe et leur classe et afficher la moyenne

grâce à la fonction groupby() et mean () pour la moyenne 

10. on fait un traitement de donnée sur notre dataFrame 

afficher la moayenne age de tout les mineurs groupé par leur genre et leurs classe

11. utiliser iloc pour localiser une donnée selon les lignes

12. utiliser loc pour localiser une donnée selon les colonnes

