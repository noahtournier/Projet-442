# -*- coding: utf-8 -*-
"""
Created on Tue May 13 11:08:04 2025

@author: Noah2
"""

import pygame

###########################
#   AJOUTER COMM UART     #
###########################

case = 60
grille = 10
fenetre = case * grille
FPS = 30

b = (255, 255, 255)
g = (50, 50, 50)
m = (150, 75, 0)
j = (255, 215, 0)
n = (0, 0, 0)

damier = [
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
]

def afficher_damier(ecran, tableau):
    ecran.fill(n)
    for ligne in range(grille):
        for colonne in range(grille):
            if (ligne + colonne) % 2 == 0:
                couleur_case = b  
            else :
                couleur_case = g
            pygame.draw.rect(
                ecran,
                couleur_case,
                (colonne * case, ligne * case, case, case)
            )
            val = tableau[ligne][colonne]
            if val != 0:
                centre = (
                    colonne * case + case // 2,
                    ligne * case + case // 2
                )
                if val == 1 or val == 3:
                    couleur_pion = m
                else:
                    couleur_pion = b
                rayon = case // 2 - 8
                pygame.draw.circle(ecran, couleur_pion, centre, rayon)
                if val == 3 or val == 4:
                    pygame.draw.circle(ecran, j, centre, rayon // 2)

def affichage(damier):
    pygame.init()
    ecran = pygame.display.set_mode((fenetre, fenetre))
    pygame.display.set_caption("Damier")
    horloge = pygame.time.Clock()

    en_cours = True
    while en_cours:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

        afficher_damier(ecran, damier)
        pygame.display.flip()
        horloge.tick(FPS)

    pygame.quit()

affichage(damier)

