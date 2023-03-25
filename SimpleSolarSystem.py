import pygame
import numpy as np

# region initializing pygame
pygame.init()
screen = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()


# endregion

# region body definition
class Body:
    def __init__(self, name: str, mass: float, radius: float, color: str, centre: tuple, net_force: tuple = (0, 0)):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.centre = np.array([float(centre[0]), float(centre[1])])
        self.net_force = np.array([float(net_force[0]), float(net_force[1])])

    def draw(self):
        pygame.draw.circle(screen, self.color, self.centre, self.radius)


# endregion

# region main logic                                #centre    #net_force
bodies = np.array([Body("sun", 60250, 25, "yellow", (750, 400), (10000, 0)),
                   Body("mercury", 1.0, 2.5, "grey", (800, 400), (0, 8)),
                   Body("venus", 14.7, 5, "green", (500, 400), (0, -50)),
                   Body("earth", 18.0, 6, "blue", (900, 400), (0, 70)),
                   Body("mars", 1.9, 3.5, "red", (600, 400), (0, 10)),
                   Body("jupiter", 50, 12, "purple", (1000, 400), (0, -200))])


def move_bodies():
    global bodies

    def force(b1: Body, b2: Body):
        G = 0.05
        M = b1.mass
        m = b2.mass
        d = np.linalg.norm(b1.centre - b2.centre)
        F = G * M * m / d ** 2
        if d < b1.radius + b2.radius:
            F = -F
        return F * (b2.centre - b1.centre) / d

    for current_body in bodies:
        for body in bodies:
            if current_body != body:
                current_body.net_force += force(current_body, body)

    for body in bodies:
        body.centre += body.net_force / body.mass
        body.draw()


# endregion

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    move_bodies()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
