from random import choice

def initDessin():
    return[
"""
+-------+
|
|
|
|
|
==============
""",
"""
+-------+
|       |
|       o
|
|
|
==============
""",
"""
+-------+
|       |
|       o
|       |
|
|
==============
""",
"""
+-------+
|       |
|       o
|      -|
|
|
==============
""",
"""
+-------+
|       |
|       o
|      -|-
|
|
==============
""",
"""
+-------+
|       |
|       o
|      -|-
|      |
|
==============
""",
"""
+-------+
|       |
|       o
|      -|-
|      | |
|
==============
"""]

def initDico():
    fichier = open("Dico_jeu_pendu.txt")
    dico=[]
    for word in fichier:
        dico.append(word.replace("\n", ""))
    return dico

def game():
    # Nombre max d'essais qu'on autorise au joueur
    nbEssaisMax = 6
    # Nombre d'essais qu'il reste au joueur
    nbEssaisRestants = 6
    # Affichage du dessin du pendu correspondant
    print(initDessin()[nbEssaisMax - nbEssaisRestants])
    # Choix au hasard du mot dans le dictionnaire
    motChoisi = choice(initDico())
    # Récupération de la longueur de mot (pour des soucis de performance)
    longueurMotChoisi = len(motChoisi)
    # Mot avec les lettres trouvées par le joueur et des _ sinon
    # Par défaut, autant de tirets qu'il y a de lettres dans le mot à deviner
    motDecouvert = "_" * longueurMotChoisi
    print(motDecouvert)
    # Indicateur si la partie en cours (on l'enclenche)
    partieEnCours = True
    # Tant que la partie est en cours
    while(partieEnCours):
        # On saute des lignes pour l'affichage
        print()
        # On demande au joueur de saisir une lettre
        lettreChoisie = input("Entrez une lettre : ").upper()
        print()
        # Indicateur si la lettre est la bonne (par défaut non)
        lettreBonne = False
        # Pour chacune des positions du mot
        for placeLettre in range(longueurMotChoisi):
            # Si la lettre choisie par le joueur correspond à la lettre du mot à trouver à cette position
            if lettreChoisie == motChoisi[placeLettre]:
                # On remplace le tiret du mot partiel découvert par la lettre à cette position
                motDecouvert = motDecouvert[:placeLettre] + lettreChoisie + motDecouvert[placeLettre+1:]
                # On indique que la lettre tapée est bonne
                lettreBonne = True     
        # Si le joueur a tapé la bonne lettre
        if lettreBonne:
            # On le félicite
            print(choice(["Oui","C'est bon","Cette lettre y est","Bien joué"])) #"Vous avez trouvé une bonne lettre")
            # S'il n'y a plus de tiret dans le mot partiel découvert
            if ("_" not in motDecouvert):
                # Alors le mot a été trouvé entièrement 
                print("Félicitations, vous avez trouvé le mot mystère")
                # et la partie est terminée
                partieEnCours = False
        # Sinon
        else:
            # On lui indique que la lettre n'est pas bonnes
            print("Dommage, la lettre que vous avez saisie n'est pas présente dans le mot")
            # On lui retire un essai restant
            nbEssaisRestants -=1
            # et s'il ne lui reste plus d'essai
            if nbEssaisRestants == 0:
                # On lui indique qu'il a perdu,
                print("Trop tard, vous avez perdu")
                # le mot à trouver
                print("Le mot à trouver était " + motChoisi)
                # et la partie est terminée
                partieEnCours = False
        # Affichage du dessin du pendu correspondant
        print(initDessin()[nbEssaisMax - nbEssaisRestants])
        # et le mot partiellement trouvé
        print(motDecouvert)

game()
