# Mancala

Jeu de Mancala pour 2 joueurs, en Python, qui se joue dans la console.

## Lancer le jeu

Il faut avoir [Python 3](https://www.python.org/downloads/) installé, puis :

```
python mancala.py
```

## Le plateau

Le plateau a 14 cases :

- 6 trous pour chaque joueur, avec 4 graines dans chaque trou au début
- 1 grenier pour chaque joueur, vide au début

```
J2 : 4 4 4 4 4 4
Grenier J2 : 0    Grenier J1 : 0
J1 : 4 4 4 4 4 4
```

Les trous du joueur 2 sont affichés à l'envers, comme sur un vrai plateau.

## Règles

1. Le joueur 1 commence.
2. À son tour, le joueur choisit un de ses trous (de 1 à 6) et prend toutes les graines qui sont dedans.
3. Il pose ensuite les graines une par une dans les cases suivantes. Il passe par les greniers et fait le tour du plateau si besoin.
4. C'est ensuite au tour de l'autre joueur.
5. La partie s'arrête quand un des deux joueurs n'a plus de graines dans ses trous.

## Score

Chaque joueur marque les graines de son grenier, plus les graines qui restent dans ses trous. Le joueur qui a le plus grand score gagne.

## Version simplifiée

Cette version ne contient pas certaines règles du Mancala classique :

- pas de tour bonus quand la dernière graine tombe dans son grenier
- pas de capture des graines adverses
- les graines peuvent aussi tomber dans le grenier de l'adversaire
- le jeu ne vérifie pas ce que tape le joueur : il faut choisir un nombre de 1 à 6 et un trou qui contient des graines
