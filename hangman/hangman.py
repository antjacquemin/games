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
    """ Initialise et retourne un dictionnaire à partir d'un fichier texte """
    fichier = open("Dico_jeu_pendu.txt")
    dico = []
    for word in fichier:
        dico.append(word.replace("\n", ""))
    return dico

def supprLong(dico, secret):
    """ 
    Supprime du dictionnaire les mots de même longueur que le mot mystère

    Parameters:
        dico (list): le dictionnaire actuel
        secret (string): le mot mystère
    Returns:
        newDico (list): un nouveau dictionnaire avec les mots supprimés
    """
    newDico = dico.copy()
    for word in dico:
        if len(word) != len(secret):
            newDico.remove(word)
    #newdico = [word in dico if len(word) == len(secret)]
    return newDico

def supprLettre(dico, lettre):
    """ 
    Supprime du dictionnaire les mots qui possèdent la lettre donnée
    
    Parameters:
        dico (list): le dictionnaire actuel
        lettre (string): la lettre considérée
    Returns:
        newDico (list): un nouveau dictionnaire avec les mots supprimés
    """
    newDico = dico.copy()
    for word in dico:
        if lettre in word:
            newDico.remove(word)
    return newDico

def supprImpossible(dico, connu, lettre):
    """ 
    Supprime du dictionnaire les mots qui ne possèdent pas la même lettre aux mêmes emplacement que le mot connu
    
    Parameters:
        dico (list): le dictionnaire actuel
        connu (string): le mot avec les lettre actuellement découvertes par le joueur
        lettre (string): la lettre considérée (la dernière lettre proposée)
    Returns:
        newDico (list): un nouveau dictionnaire avec les mots supprimés
    """
    newDico = dico.copy()
    for word in dico:
        for ind, char in enumerate(connu):
            if char == lettre:
                if word[ind] != lettre:
                    newDico.remove(word)
                    break
            elif char == "_":
                if word[ind] == lettre:
                    newDico.remove(word)
                    break
    return newDico

def suggest(dico, connu):
    """ 
    Suggère une lettre parmi celles possibles 
    
    Parameters:
        dico (list): le dictionnaire actuel
        connu (string): le mot avec les lettre actuellement découvertes par le joueur
    Returns:
        char (string): la lettre suggérée
    """
    for ind, char in enumerate(connu):
        if char == "_":
            return dico[0][ind]

def best(dico, connu):
    """ 
    Suggère la meilleure lettre possible (statistiquement) parmi celles possibles 
    
    Parameters:
        dico (list): le dictionnaire actuel
        connu (string): le mot avec les lettre actuellement découvertes par le joueur
    Returns:
        char (string): la lettre suggérée
    """
    occurences = {}
    for ind, caractere in enumerate(connu):
        if caractere == "_":
            for mot in dico:
                lettrePossible = mot[ind]
                if lettrePossible in occurences:
                    occurences[lettrePossible] += 1
                else:
                    occurences[lettrePossible] = 1
    return sorted(occurences.items(), key=lambda item: item[1])[-1][0]

def game():
    # Nombre max d'essais qu'on autorise au joueur
    nbEssaisMax = 6
    # Nombre d'essais qu'il reste au joueur
    nbEssaisRestants = 6
    # Affichage du dessin du pendu correspondant
    print(initDessin()[nbEssaisMax - nbEssaisRestants])
    dico = initDico()
    # Choix au hasard du mot dans le dictionnaire
    motChoisi = choice(dico)
    # Récupération de la longueur de mot (pour des soucis de performance)
    longueurMotChoisi = len(motChoisi)
    #print(len(dico))
    dico = supprLong(dico, motChoisi) # TODO Englober dans decorator
    #print(len(dico))
    # Mot avec les lettres trouvées par le joueur et des _ sinon
    # Par défaut, autant de tirets qu'il y a de lettres dans le mot à deviner
    motDecouvert = "_" * longueurMotChoisi
    print(motDecouvert)
    # Dicionnaire des accents existants en français (avec la lettre non accentuée en clé)
    accents = {"A": "ÀÂÄ", "E": "ÉÈÊË", "I": "ÎÏ", "O": "ÔÖ", "U": "ÙÛÜ", "C": "Ç"}
    # Ensemble des lettres proposées par le joueur
    lettresProposees = set()
    # Indicateur si la partie en cours (on l'enclenche)
    partieEnCours = True
    # Tant que la partie est en cours
    while(partieEnCours):
        # On saute des lignes pour l'affichage
        print()
        # On demande au joueur de saisir une lettre
        lettreChoisie = input("Entrez une lettre (help ou aide pour obtenir la suggestion de l'ordinateur) : ")
        # indicateur du respect du format entré par le joueur (par défaut non)
        bonFormat = False
        # Tant que ce n'est pas le bon format
        while (not bonFormat):
            # Si le joueur a tapé une lettre (ou des lettres)
            if lettreChoisie.isalpha():
                # On met sa saisie en majuscules
                lettreChoisie = lettreChoisie.upper()
                # S'il n'a tapé qu'une lettre
                if (len(lettreChoisie) == 1):
                    # On regarde si la lettre est accentuée en parcourant le dictionnaire
                    for cle, groupe in accents.items():
                        if lettreChoisie in groupe:
                            # On la remplace dans ce cas par la lettre non accentuée
                            lettreChoisie = cle
                    # Si la lettre tapée est dans les lettres proposées
                    if lettreChoisie in lettresProposees:
                        # On demande au joueur de saisir une autre lettre
                        lettreChoisie = input("Vous avez déjà proposé cette lettre, entrez-en une autre : ")
                    # Sinon tout est bon et on peut passer à la suite
                    else:
                        bonFormat = True
                # S'il a tapé aide ou help
                elif lettreChoisie == "AIDE" or lettreChoisie == "HELP":
                    # On lui suggère la meilleure possibilité
                    lettreChoisie = best(dico, motDecouvert)
                    # En le lui indiquant
                    print("Choix de l'ordinateur : ", lettreChoisie)
                else:
                    lettreChoisie = input("Entrez une seule lettre : ")
            else:
                lettreChoisie = input("Entrez une LETTRE : ")
        lettresProposees.add(lettreChoisie)
        #print(lettresProposees)
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
            #print(len(dico))
            dico = supprImpossible(dico, motDecouvert, lettreChoisie)
            # On le félicite
            print(choice(["Oui","C'est bon","Cette lettre y est","Bien joué"])) #"Vous avez trouvé une bonne lettre")
            #print(len(dico))
            #print(dico)
            # S'il n'y a plus de tiret dans le mot partiel découvert
            if ("_" not in motDecouvert):
                # Alors le mot a été trouvé entièrement 
                print("Félicitations, vous avez trouvé le mot mystère")
                # et la partie est terminée
                partieEnCours = False
        # Sinon
        else:
            #print(len(dico))
            dico = supprLettre(dico, lettreChoisie)
            # On lui indique que la lettre n'est pas bonnes
            print(choice(["Dommage, la lettre que vous avez saisie n'est pas présente dans le mot", "Raté", "Non"]))
            #print(len(dico))
            #print(dico)
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
