# Identification et extraction d’informations textuelles dans un corpus médiatique
## cherche_spoilers_CHEVAL.py
Correspond au code python du projet.
Pour que le fichier fonctionne correctement, veillez à :
- [ ] Télécharger et importer le jeu de données *validation.json*.
- [ ] Télécharger toutes les bibiliothèques nécessaires.

## mot_en_commun.csv
Fichier de sortie de *cherche_spoilers_CHEVAL.py*.

L'espacement des colonnes se fait avec le symbole *µ*.
Le séparateur de caractère est le symbole *|*.

## reponses_correctes_all.csv et reponses_correctes_sansmulti
Fichier qui affiche les phrases qui sont correctes avec le spoiler associé.

Le fichier *reponses_correctes_all.csv* prend tous les articles du fichier *validation.json*.
Le fichier *reponses_correctes_sansmulti.csv* prend uniquement les articles qui n'ont pas de spoilers de type "multi".

L'espacement des colonnes se fait avec le symbole *;*. 
Le séparateur de caractère est le symbole *"*.
