import pygame
import sys

pygame.init()
size = width,height = 680,500
screem = pygame.display.set_mode(size)
ball = pygame.image.load("D:\\day4\\image\\timg.jpg")
ballrect = ball.get_rect()
speed = [5,5]
clock = pygame.time.Clock()
color = (0,0,0)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screem.fill(color)
    screem.blit(ball,ballrect)
    pygame.display.flip()
pygame.quit()