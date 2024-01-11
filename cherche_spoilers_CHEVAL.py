import json
import spacy
import operator
import re
nlp = spacy.load("en_core_web_sm")

fichier_mot=open("mots_en_commun_.csv","w",encoding="UTF-8")
fichier_mot.write("postText"+"	"+"phrase(s)"+"	"+"spoiler"+"\n")
with open("validation.jsonl", encoding="UTF-8") as mon_fichier:
    # Initialiser une liste pour stocker les clés "postText" et "targetParagraphs"
    postText_and_targetParagraphs = [] 
    # Lire chaque ligne du fichier
    for ligne in mon_fichier:
        # Charger l'objet JSON à partir de la ligne
        objet_json = json.loads(ligne)
        # Vérifier si les clés "postText" et "targetParagraphs" existent
        if "postText" in objet_json and "targetParagraphs" in objet_json and "spoiler" in objet_json:
            # Ajouter les valeurs de ces clés à la liste
            postText_and_targetParagraphs.append({
                "targetParagraphs": objet_json["targetParagraphs"],
                "postText": objet_json["postText"],
                "spoiler" : objet_json["spoiler"]
            })

#normalisation des mots 
def norm(u): 
    u=u.lower()
    doc=nlp(u)
    l=[]
    for tok in doc:
        if not tok.is_punct and not tok.is_stop:
            l.append(tok.lemma_)
    return(l)

cpt=0
l_adv=["when","how much","how many","where","why","who"]
for i in postText_and_targetParagraphs:
    cpt=cpt+1
    texte_norm=norm(i["postText"][0])
    txt=i["postText"][0]
    doc_txt=nlp(txt)
    corps=i["targetParagraphs"]
    spoiler=i["spoiler"]
    comparateur={}
    for partie in corps:
        doc=nlp(partie)
        for sent in doc.sents: #découper en phrases
            c=0
            corps_norm=norm(str(sent))#normalisation des phrases ici car pas possible plus haut (on ne peut pas le faire sur une liste de lste)
            for mot in texte_norm:
                for w in corps_norm:
                    if mot==w:
                        c=c+1
                        comparateur[sent]=c #compte le nombre de mots en commun avec le texte
                        break #quand on trouve le mot dans le texte, on passe au suivant, ca permet de ne pas prendre le mot plusieurs fois
  
    if comparateur:
        #liste_p=[]
        max_key = max(comparateur.items(), key=operator.itemgetter(1))[1] 
        max_value = max(comparateur.values())
        l_mot_egal = [i[0] for i in comparateur.items() if i[1] == max_key]#liste le ou les phrases qui ont le plus de mot en commun avec le titre
        
#-----------------------------------------------------------------------------
#partie consacrée aux indices syntaxiques
 
    if len(l_mot_egal)!=1:#prendre seulement les listes qui ont plusieurs phrases
        liste_verif=[]#liste qui vérifie les phrases qu'on va garder 
        for p in l_mot_egal:
            adv=0 
            for ad in l_adv:           
                if ad in txt.lower(): #on vérifie si il y a bien un adverbe présent dans le titre
                    mot_adv=ad
                    adv=adv+1
                    
            if adv>0: #si il y a un adverbe, on regarde les particularités pour chaque adverbe dans les phrases
                if mot_adv=="how much" or mot_adv=="how many"or mot_adv=="when":
                    if re.findall(r"[0-9+]",str(p)): #chercher la présence de nombre dans les phrases
                        liste_verif.append("1")
                    else:
                        liste_verif.append("0")
                elif mot_adv=="where":
                    doc_p=nlp(str(p))
                    for en in doc_p.ents:
                        if en.label_=="LOC": #chercher les E.N de lieu 
                            liste_verif.append("1")
                        else:
                            liste_verif.append("0")
                else:
                    liste_verif.append("0")
                    #Par soucis de temps, tous les adverbes n'ont pas pu être réalisés        
                            
        if "1" not in liste_verif:
            print("rien")
            fichier_mot.write(txt+"	"+str(l_mot_egal)+"	"+spoiler[0]+"\n")
        else:
            l_mot_modif=[]
            l_mot_modif = l_mot_modif = [x for i, x in enumerate(l_mot_egal) if i < len(liste_verif) and liste_verif[i] == "1"]
            fichier_mot.write(txt+"	"+str(l_mot_modif)+"	"+spoiler[0]+"\n")
            print("APRES",l_mot_modif)
    
    else: #garder les phrases uniques et les inserer dans le fichier csv
        print("ok")
        fichier_mot.write(txt+"	"+str(l_mot_egal)+"	"+spoiler[0]+"\n")
fichier_mot.close()