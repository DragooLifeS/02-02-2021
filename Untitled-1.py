import pygame
pygame.init()

W = 500
H = 500
x = W // 2
y = H // 2

c1 = (2, 100, 55)
c2 = (2, 0 , 55)
c3 = (0 , 0, 150)

sc = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(c1)
    pygame.draw.circle(sc, c2,(x, y), 20)
    pygame.draw.rect(sc, c3,(x, y, 100, 100), 5)
    pygame.draw.line(sc, ((255, 255, 255)), (0, 0), (W,H), 5)
    pygame.draw.line(sc, ((255, 255, 255)), (W, 0), (0,H), 5)
    pygame.display.update()

