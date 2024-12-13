#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Rappelez votre nom ici au cas où : 

from graphique_jeu import *
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, QUIT

from random import randint


### Vos fonctions ci-dessous

def cree_listes(taillex, tailley, nbre):
    """ 
    taillex, tailley : dimensions de l'écran de jeu
    nbre : nombre de carrés voulus
    crée deux listes lx et ly de carrés mobiles en début de jeu,
    et les renvoie"""
    # votre code ici
    pass



############ Fonction du jeu

def jeu(taillex, tailley):
    """ taillex et tailley sont les dimensions du jeu souhaitées
    Règles du jeu : """

    ###### Initialisation du jeu #######

    delai = ...  # délai en secondes entre deux mouvements des objets mobiles

    # création des objets mobiles en début de jeu (combien ?)
    lx, ly = cree_listes(taillex, tailley, ...)
    
    # Initialisation de x et y les coordonnées du carré perso
    x = ...
    y = ...
    
    # Autres initialisation (score, points de vie, ... ?)
    
    
    # Cette variable pourra passer à False quand on aura perdu (ou qu'on voudra
    # arrêter le jeu)
    continuer = True
    t = 0 # temps écoulé depuis le délai, ne pas modifier 


    ###### Boucle principale du jeu #######
    while continuer:
        # Gestion des évènements
        for event in pygame.event.get(): # Si on quitte
            if event.type == pygame.QUIT: 
                pygame.quit()
                return
            # Si touche appuyée
            if event.type == pygame.KEYDOWN:
                if event.key== K_LEFT:
                    # appui sur la touche "gauche"
                    # le carré perso se déplace à gauche
                    pass
                elif event.key == K_RIGHT:
                    # appui sur la touche "droite"
                    pass
                elif event.key == K_UP:
                    # appui sur la touche "haut"
                    pass
                elif event.key == K_DOWN:
                    pass

        # Gestion des collisions
        # On récupère l'indice de collision dans i_coll
        i_coll = collision(lx, ly, x, y)
        # À vous de jouer, que se passe-t-il s'il y a collision

        t = t+1/fps # temps passé
        if t > delai: # si on a passé le délai, on fait bouger les objets
            # et il peut se passer autre chose (au choix)
            t = 0
            bouge(taillex, tailley, lx, ly)
        
        # Autres événements qui peuvent se passer à chaque nouvelle frame
    
        affiche_jeu(...) # à compléter !
    
        # permet de ne pas aller plus vite que fps frames par seconde
        clock.tick(fps)    
        
    # Si on sort de la boucle, c'est qu'on a perdu (ou autre). Afficher alors
    # quelque chose ?
    
    

# Lancement du jeu
jeu(15, 15)
