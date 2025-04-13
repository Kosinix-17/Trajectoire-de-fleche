import math
import pygame


class Fleche:
    def __init__(self, WIDTH, HEIGHT, mouse_pos, time):
        self.time_start = time
        self.time = 0
        self.x_end = mouse_pos[0]
        self.y_end = mouse_pos[1]
        self.gravity = 300  # Augmenter pour un effet plus réaliste
        self.angle = math.radians(-45)  # Convertir directement en radians
        self.x_init = WIDTH // 8
        self.y_init = HEIGHT // 4
        self.x = self.x_init
        self.y = self.y_init

        # Calcule de la distance entre le point de départ et le point d'arrivée
        distance_point_arrive = math.sqrt(
            (self.x_end - self.x_init) ** 2 + (self.y_end - self.y_init) ** 2
        )

        # Calcul du temps d'arrivée basé sur la distance (arbitrairement divisé par 300 pour équilibrer)
        self.temps_arrive = max(0.1, distance_point_arrive / 300)

        # Calcul des vitesses initiales
        self.vx = (self.x_end - self.x_init) / self.temps_arrive
        self.vy = (self.y_end - self.y_init) / self.temps_arrive - 0.5 * self.gravity * self.temps_arrive

    def position(self, time):
        self.time = (time - self.time_start) / 1000  # Convertir le temps en secondes
        if self.time >= 0:
            self.x = self.x_init + self.vx * self.time
            self.y = self.y_init + self.vy * self.time + 0.5 * self.gravity * self.time ** 2
        return self.y >= screen.get_height() - 5  # Retourne si la flèche est hors de l'écran


pygame.init()

# Création de la fenêtre
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation de trajectoire")
clock = pygame.time.Clock()  # Pour limiter les FPS

Ensemble_fleche = []

running = True
while running:
    screen.fill((255, 255, 255))
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            Ensemble_fleche.append(Fleche(WIDTH, HEIGHT, mouse_pos, time))

    # Gérer les flèches existantes
    for fleche in Ensemble_fleche[:]:
        if not fleche.position(time):
            # Dessiner la flèche
            pygame.draw.circle(screen, (0, 0, 255), (int(fleche.x), int(fleche.y)), 5)
        else:
            # Supprimer la flèche qui sort de l'écran
            Ensemble_fleche.remove(fleche)

    pygame.display.flip()
    clock.tick(60)  # Limiter à 60 FPS
