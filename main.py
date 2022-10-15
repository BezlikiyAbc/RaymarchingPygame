import pygame
from pygame import *
import math

width = 1280
height = 960

PlayerPosition = [width/2, height/2]
Angle = 0

pygame.init()
pygame.display.set_caption('Raymarching')
screen = pygame.display.set_mode( (width, height) )
clock = pygame.time.Clock()


def RotZ(pos, angle):
	return [pos[0] * math.cos(angle) - pos[1] * math.sin(angle), pos[0] * math.sin(angle) + pos[1] * math.cos(angle)]

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	screen.fill((0,0,0))

	pygame.draw.circle(screen, (200,200,200),PlayerPosition, 10)
	pygame.draw.line(screen, (255,255,255), PlayerPosition,(PlayerPosition[0] + 100, PlayerPosition[1]), 3)

	AnglePos = RotZ((100, 0), Angle * math.pi/180)

	pygame.draw.line(screen, (255,0,0), PlayerPosition,(AnglePos[0] + PlayerPosition[0],AnglePos[1]+PlayerPosition[1]), 1)

	#Angle += 5

	pygame.display.update()
	clock.tick(10)