import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Paramètres de la fenêtre
largeur, hauteur = 1000, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Pygame - Évitez les obstacles")

# Chargement des images
personnage_image = pygame.image.load("personnage.png")
personnage_image = pygame.transform.scale(personnage_image, (100, 100))  # Redimensionner l'image du personnage
obstacle_image = pygame.image.load("obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (150, 150))  # Redimensionner l'image de l'obstacle

# Position initiale du personnage
personnage_x = largeur // 2 - 25
personnage_y = hauteur - 100

# Position initiale de l'obstacle
obstacle_x = random.randint(0, largeur - 150)
obstacle_y = -150
obstacle_vitesse = 20

# Boucle principale
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement du personnage avec les touches fléchées
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and personnage_x > 0:
        personnage_x -= 15
    if touches[pygame.K_RIGHT] and personnage_x < largeur - 50:
        personnage_x += 15

    # Déplacement de l'obstacle vers le bas
    obstacle_y += obstacle_vitesse

    # Réinitialisation de l'obstacle s'il atteint le bas de l'écran
    if obstacle_y > hauteur:
        obstacle_x = random.randint(0, largeur - 150)
        obstacle_y = -150

    # Vérification de la collision entre le personnage et l'obstacle
    if (
        personnage_x < obstacle_x + 150
        and personnage_x + 150 > obstacle_x
        and personnage_y < obstacle_y + 150
        and personnage_y + 150 > obstacle_y
    ):
        print("Collision !")
        pygame.quit()
        sys.exit()

    # Effacer l'écran
    fenetre.fill(BLANC)

    # Afficher le personnage et l'obstacle
    fenetre.blit(personnage_image, (personnage_x, personnage_y))
    fenetre.blit(obstacle_image, (obstacle_x, obstacle_y))

    pygame.display.flip()

    # Réguler la vitesse de la boucle
    clock.tick(30)
