# MANCALA - jeu pour 2 joueurs
# (les lignes qui commencent par # sont des commentaires : Python ne les lit pas)

# Plateau : 14 cases
#   0 a 5  = trous du joueur 1     6  = grenier du joueur 1
#   7 a 12 = trous du joueur 2     13 = grenier du joueur 2

# On cree le plateau : une liste de 14 nombres (= nombre de graines dans chaque case)
# 4 graines dans chaque trou, 0 dans les greniers au debut
plateau = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

# Cette variable retient a qui c'est le tour : le joueur 1 commence
joueur = 1

# "while" = "tant que" : tout ce qui est decale en dessous se repete
# sum(plateau[0:6]) = total des graines du joueur 1 (cases 0 a 5)
# sum(plateau[7:13]) = total des graines du joueur 2 (cases 7 a 12)
# Donc on joue TANT QUE les deux joueurs ont encore des graines
while sum(plateau[0:6]) > 0 and sum(plateau[7:13]) > 0:

    # ----- Afficher le plateau -----

    # Affiche une ligne vide pour aerer l'ecran
    print()
    # Affiche les trous du joueur 2 a l'envers (12 vers 7) pour faire comme un vrai plateau
    print("J2 :", plateau[12], plateau[11], plateau[10], plateau[9], plateau[8], plateau[7])
    # Affiche les deux greniers : case 13 (joueur 2) et case 6 (joueur 1)
    print("Grenier J2 :", plateau[13], "   Grenier J1 :", plateau[6])
    # Affiche les trous du joueur 1 dans l'ordre (0 a 5)
    print("J1 :", plateau[0], plateau[1], plateau[2], plateau[3], plateau[4], plateau[5])

    # ----- Choisir un trou -----

    # input() pose la question et attend que le joueur tape quelque chose
    # str(joueur) transforme le nombre 1 ou 2 en texte pour l'afficher dans la phrase
    # int() transforme ce que le joueur a tape (du texte) en nombre
    # Le nombre tape est range dans la variable "choix"
    choix = int(input("Joueur " + str(joueur) + ", choisis un trou (1 a 6) : "))

    # Si c'est le joueur 1...
    if joueur == 1:
        # ... trou 1 = case 0, trou 6 = case 5, donc on enleve 1
        case = choix - 1
    # Sinon (c'est le joueur 2)...
    else:
        # ... trou 1 = case 7, trou 6 = case 12, donc on ajoute 6
        case = choix + 6

    # ----- Prendre les graines -----

    # On regarde combien de graines il y a dans le trou choisi (on les prend dans la main)
    graines = plateau[case]
    # On vide le trou : il y a maintenant 0 graine dedans
    plateau[case] = 0

    # ----- Poser les graines une par une -----

    # On repete TANT QU'il reste des graines dans la main
    while graines > 0:
        # On avance d'une case
        case = case + 1
        # Si on depasse la derniere case (13)...
        if case == 14:
            # ... on revient au debut du plateau (on fait le tour)
            case = 0
        # On pose une graine dans cette case (on ajoute 1)
        plateau[case] = plateau[case] + 1
        # On a une graine de moins dans la main (on enleve 1)
        graines = graines - 1

    # ----- Changer de joueur -----

    # Si c'etait le joueur 1...
    if joueur == 1:
        # ... maintenant c'est le joueur 2
        joueur = 2
    # Sinon (c'etait le joueur 2)...
    else:
        # ... maintenant c'est le joueur 1
        joueur = 1

    # Ici on remonte en haut du "while" pour le tour suivant

# ----- Fin de la partie -----
# (on arrive ici quand un des deux joueurs n'a plus de graines)

# Affiche une ligne vide pour aerer
print()
# Score du joueur 1 = son grenier (case 6) + les graines restantes dans ses trous (0 a 5)
print("Score J1 :", plateau[6] + sum(plateau[0:6]))
# Score du joueur 2 = son grenier (case 13) + les graines restantes dans ses trous (7 a 12)
print("Score J2 :", plateau[13] + sum(plateau[7:13]))
