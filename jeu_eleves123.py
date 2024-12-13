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
    # les blocs apparaissent de facon aleatoir
    lx=[0]*nbre
    ly=[0]*nbre
    for i in range(len(lx)):
        lx[i]=lx[i]+randint(1,taillex)-1
        ly[i]=ly[i]+randint(1,tailley)-1
    return lx,ly


def bouge(taillex,tailley,lx,ly):
    """
    taillex, tailley : dimensions de l'écran de jeu
    lx,ly : sont des listes remplis des positions des cubes
    permet au carrés mobiles de bouger selon un certzin patern.
    """
    for i in range(len(lx)):
        #les blocs bouges de manière aleatoire
        if lx[i] <= taillex-2 and lx[i] >= 1: 
            lx[i]=randint(0,taillex-1)
        elif lx[i]>taillex-2 :
            lx[i]=randint(1,taillex)-1#le bloc est trop pret de la ligne droite le cube se teleporte de manire aleatoire
        elif lx[i]<1 :
            lx[i]=randint(1,taillex)-1#le bloc est trop pret de la ligne droite le cube se teleporte de manire aleatoire
            
    for i in range(len(ly)):#le bloc est trop pret de la ligne du bas le cube se teleporte vers le haut
        if ly[i]<tailley-1:
            ly[i]=ly[i]+1
        else:
            ly[i]=0
    
        
def collision(lx,ly,x,y):
    """
    lx,ly : sont des listes remplis des positions des cubes
    permet au carrés mobiles de bouger selon un certzin patern.
    x,y : sont les coordonnées du cube " joueurs "
    Cette fonctiondetecte si le cube "joueur" est au meme coordonné qu' un blocs mobile.
    """
    indice=-1
    for i in range(len(lx)):
        if x==lx[i] and y==ly[i]:
            indice=lx[i]
    return indice
            

############ Fonction du jeu

def jeu(taillex, tailley):
    """ taillex et tailley sont les dimensions du jeu souhaitées
    Règles du jeu : Le cube joueur bleu doit éviter les carrés rouges sion il perd des vies,
    le joueur gagne un point apres chaque seconde passé en vie"""

    ###### Initialisation du jeu #######
    nbre= 3#nbre est le nombre de blocs mobile. Il y a autant de cube que
    #taille de x
    delai = 1  # délai en secondes entre deux mouvements des objets mobiles

    # création des objets mobiles en début de jeu (combien ?)
    lx,ly=cree_listes(taillex, tailley, nbre)
    
    # Initialisation de x et y les coordonnées du carré perso
    # le carré va apparaitre au centre de l'ecran
    x = taillex//2 
    y = tailley//2
    
    # Autres initialisation (score, points de vie, ... ?)
    score=0
    pv=3 #pv= point de vie
    
    # Cette variable pourra passer à False quand on aura perdu (ou qu'on voudra
    # arrêter le jeu)
    continuer = True# le jeu demare
    
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
                if event.key== K_LEFT and  x > 0: #si la touche appuiyez est la touche gauche et que x => 1 le carré va sui la gauche
                    x= x-1
                elif event.key == K_RIGHT and x < taillex-1:#si la touche appuiyez est la touche droite et que x < a la limite de l'ecran le carré va sur droite
                    x=x+1
                elif event.key == K_UP and y > 0: #si la touche appuiyez est la touche haut et que y => 1 le carré va sur la haut
                    y=y-1
                elif event.key == K_DOWN and y < taillex-1 : #si la touche appuiyez est la touche droite et que y < a la limite de l'ecran le carré va ver le bas
                    y=y+1

        # Gestion des collisions
        # On récupère l'indice de collision dans i_coll
        i_coll = collision(lx, ly, x, y)
        if i_coll != -1: #si il n'y a pas eu de collision
            pv= pv-1 # le joueur perd un point de vie
            #le joueur est de retour au centre
            x=taillex//2 
            y=tailley//2
            #aucun bloc ne peut apparaitre dans une zone de 3*3 autour du centre pendant une sec
            for i in range (len(lx)):
                if lx[i]== taillex//2 and ly[i]==tailley//2 :
                    lx[i]=0
                    ly[i]=0
                elif lx[i]== (taillex//2)+1 and (ly[i]==tailley//2) :
                    lx[i]=taillex+1-taillex
                    ly[i]=0
                elif lx[i]== (taillex//2) and (ly[i]==tailley//2)-1 :
                    lx[i]=taillex+2-taillex
                    ly[i]=0
                elif lx[i]== (taillex//2) and (ly[i]==tailley//2)+1 :
                    lx[i]=taillex+3-taillex
                    ly[i]=0
                elif lx[i]== (taillex//2)-1 and (ly[i]==tailley//2) :
                    lx[i]=taillex+4-taillex
                    ly[i]=0
                elif lx[i]== (taillex//2)+1 and (ly[i]==tailley//2)-1 :
                    lx[i]=taillex+5-taillex
                    ly[i]=0
                elif lx[i]== (taillex//2)-1 and (ly[i]==tailley//2)-1 :
                    lx[i]=taillex+6-taillex
                    ly[i]=0
                elif lx[i]== (taillex//2)+1 and (ly[i]==tailley//2)+1 :
                    lx[i]=taillex+7-taillex
                    ly[i]=0
                elif lx[i]== (taillex//2)-1 and (ly[i]==tailley//2)+1 :
                    lx[i]=taillex+8-taillex
                    ly[i]=0
                    

        t = t+1/fps # temps passé
        if t > delai: # si on a passé le délai, on fait bouger les objets
            
            t = 0
            nbre = nbre +1 # chaque seconde le nombre de cub augmente de 1
            #la taille de l'ecran diminue de 1 a chaqe frame mais ce bloc a taillex=6 et tailley=6
            if taillex>7 and tailley>7 :
                taillex=taillex-1
                tailley= tailley-1
            
            # si carré est superieur ou egale a taillex-1 le carré se deplace de 1 sur la gauche
            if x>= taillex-1:
                x=x-1
            # si carré est inferieur ou egale a 1 le carré se deplace de 1 sur la droite
            if x<= 1:
                x=x+1
            # si carré est inferieur ou egale a 1 le carré se deplace de 1 vers le bas
            if y<=1:
                y=y+1
            # si carré est superieur ou egale a tailley-1 le carré se deplace de 1 vers le haut       
            if y>= tailley-1:
                y=y-1
                
            lx,ly=cree_listes(taillex, tailley, nbre)
            bouge(taillex,tailley,lx,ly)# a chaque seconde les carré mobiles bouges
            score = score + 1# le score augmente toute les secondes
            
            
        # Autres événements qui peuvent se passer à chaque nouvelle frame
        if pv <= 0 : #si le joeuur a 0 vie ou moins
            continuer= False # le jeu s'arrete
        
        
        #chaque seconde 
        affiche_jeu(taillex,tailley,lx,ly,x,y,["score : "+ str (score),"","vie : "+ str (pv),]) # à compléter !
    
        # permet de ne pas aller plus vite que fps frames par seconde
        clock.tick(fps)    
        
    # Si on sort de la boucle, c'est qu'on a perdu.
    while continuer == False : #si le jeu est perdu
        #le jeu affiche 
        affiche_jeu(taillex,tailley,lx,ly,x,y,["score : "+ str (score) + "  GAME OVER"])
        for event in pygame.event.get(): # Si on quitte
            if event.type == pygame.QUIT: 
                pygame.quit()
                return 
            
    

# Lancement du jeu
jeu(20, 20)
