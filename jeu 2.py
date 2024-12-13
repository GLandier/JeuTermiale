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
    lx=[0]*nbre
    ly=[0]*nbre
    for i in range(len(lx)):
        lx[i]=randint(1,taillex)-1
        ly[i]=randint(1,tailley)-1
    return lx,ly

def bouge(taillex,tailley,lx,ly):
    for i in range (len(lx)):
        lx[i]=randint(1,taillex)-1
        ly[i]=randint(1,tailley)-1
    return lx, ly
    


def collision(lx,ly,x,y):
    for i in range(len(lx)):
        if x==lx[i] and y==ly[i]:
            return True
            
    
        



        
    

############ Fonction du jeu

def jeu(taillex, tailley):
    """ taillex et tailley sont les dimensions du jeu souhaitées
    Règles du jeu : """

    ###### Initialisation du jeu #######
    nbre= 1
    delai = 1  # délai en secondes entre deux mouvements des objets mobiles

    # création des objets mobiles en début de jeu (combien ?)
    lx,ly=cree_listes(taillex, tailley, nbre)
    
    # Initialisation de x et y les coordonnées du carré perso
    x = taillex//2
    y = tailley//2
    
    # Autres initialisation (score, points de vie, ... ?)
    score= 0
    temps= 60

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
                if event.key== K_LEFT and  x > 0:
                    x= x-1
                    # appui sur la touche "gauche"
                    # le carré perso se déplace à gauche
                elif event.key == K_RIGHT and x < taillex-1:
                    # appui sur la touche "droite"
                    x=x+1
                elif event.key == K_UP and y > 0:
                    # appui sur la touche "haut"
                    y=y-1
                elif event.key == K_DOWN and y < taillex-1 :
                    y=y+1

        # Gestion des collisions
        # On récupère l'indice de collision dans i_coll
        i_coll = collision(lx, ly, x, y)
        if i_coll == True:
            score = score + 1
            bouge(taillex, tailley, lx, ly)
            
            

        # À vous de jouer, que se passe-t-il s'il y a collision

        t = t+1/fps # temps passé
        if t > delai: # si on a passé le délai, on fait bouger les objets
            # et il peut se passer autre chose (au choix)
            t = 0
            temps = temps - 1
            
            
        # Autres événements qui peuvent se passer à chaque nouvelle frame
        if temps <= 0 :
            continuer= False 
        
        affiche_jeu(taillex,tailley,lx,ly,x,y,["score : "+ str (score) + "  temps : "+ str (temps)]) # à compléter !
    
        # permet de ne pas aller plus vite que fps frames par seconde
        clock.tick(fps)    
        
    # Si on sort de la boucle, c'est qu'on a perdu (ou autre). Afficher alors
    # quelque chose ?
    while continuer == False :
        for event in pygame.event.get(): # Si on quitte
            if event.type == pygame.QUIT: 
                pygame.quit()
                return 
        affiche_jeu(taillex,tailley,lx,ly,x,y,["score : "+ str (score) + "  GAME OVER"])
    

# Lancement du jeu
jeu(15, 15)
