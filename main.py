import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de plateforme")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

# Variables du joueur
joueur_largeur = 40
joueur_hauteur = 60
joueur_x = 50
joueur_y = hauteur - joueur_hauteur
joueur_vitesse = 5

# Variables des objets
objet_taille = 20
objet_x = random.randint(0, largeur - objet_taille)
objet_y = -objet_taille
objet_vitesse = 3

# Variables des obstacles
obstacle_largeur = 80
obstacle_hauteur = 20
obstacle_x = random.randint(0, largeur - obstacle_largeur)
obstacle_y = -obstacle_hauteur
obstacle_vitesse = 4

# Variables du score
score = 0
font = pygame.font.Font(None, 36)

# Boucle de jeu
en_cours = True
clock = pygame.time.Clock()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Mouvement du joueur
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and joueur_x > 0:
        joueur_x -= joueur_vitesse
    if touches[pygame.K_RIGHT] and joueur_x < largeur - joueur_largeur:
        joueur_x += joueur_vitesse

    # Mouvement de l'objet
    objet_y += objet_vitesse
    if objet_y > hauteur:
        objet_x = random.randint(0, largeur - objet_taille)
        objet_y = -objet_taille
        score += 10
        objet_vitesse += 0.5

    # Mouvement de l'obstacle
    obstacle_y += obstacle_vitesse
    if obstacle_y > hauteur:
        obstacle_x = random.randint(0, largeur - obstacle_largeur)
        obstacle_y = -obstacle_hauteur

    # Collision entre le joueur et l'objet
    if joueur_x < objet_x + objet_taille and joueur_x + joueur_largeur > objet_x and joueur_y < objet_y + objet_taille and joueur_y + joueur_hauteur > objet_y:
        objet_x = random.randint(0, largeur - objet_taille)
        objet_y = -objet_taille
        score += 10
        objet_vitesse += 0.5

    # Collision entre le joueur et l'obstacle
    if joueur_x < obstacle_x + obstacle_largeur and joueur_x + joueur_largeur > obstacle_x and joueur_y < obstacle_y + obstacle_hauteur and joueur_y + joueur_hauteur > obstacle_y:
        en_cours = False

    # Dessiner l'écran
    ecran.fill(BLANC)
    pygame.draw.rect(ecran, NOIR, (joueur_x, joueur_y, joueur_largeur, joueur_hauteur))
    pygame.draw.rect(ecran, ROUGE, (objet_x, objet_y, objet_taille, objet_taille))
    pygame.draw.rect(ecran, NOIR, (obstacle_x, obstacle_y, obstacle_largeur, obstacle_hauteur))
    
    # Affichage du score
    score_texte = font.render("Score: " + str(score), True, NOIR)
    ecran.blit(score_texte, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

# Quitter Pygame
pygame.quit()

