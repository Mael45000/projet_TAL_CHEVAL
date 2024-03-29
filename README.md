# Identification et extraction d’informations textuelles dans un corpus médiatique
## cherche_spoilers_CHEVAL.py
Correspond au code python du projet.
Pour que le fichier fonctionne correctement, veillez à :
- [ ] Télécharger et importer le jeu de données "validation.jsonl" de la campagne Semeval 2023 task 5 : "clickbait spoiling", disponible à cette adresse :  https://zenodo.org/records/6362726#.YsbdSTVBzrk
- [ ] Télécharger toutes les bibiliothèques nécessaires.

## sortie_cherche_spoilers.csv
Fichier de sortie de *cherche_spoilers_CHEVAL.py*.

L'espacement des colonnes se fait avec le symbole *µ*.
Le séparateur de caractère est le symbole *|*.

## reponses_correctes_all.csv et reponses_correctes_sansmulti
Fichier qui affiche les phrases qui sont correctes avec le spoiler associé.

Le fichier *reponses_correctes_all.csv* prend en compte tous les articles du fichier *validation.json*.
Le fichier *reponses_correctes_sansmulti.csv* prend uniquement les articles qui n'ont pas de spoilers de type "multi".

L'espacement des colonnes se fait avec le symbole *;*. 
Le séparateur de caractère est le symbole *"*.
