# Write your code here :-)
import pygame as pg

from sys import path
from sys import exit
import os
import expy as ex
import random

#Setup

pg.init()
screen = pg.display.set_mode((800,600)) #set your window size
pg.display.set_caption("Flappy Bird")
clock = pg.time.Clock()

#colours
black = (0,0,0)
white = (255,255,255)
green = (0,200,0)
red = (200,0,0)
orange = (255, 175,0)

bird_pic = pg.Surface((95,60),pg.SRCALPHA, 32)

#bird drawing
pg.draw.ellipse(bird_pic, orange, (70,25,25,15))
pg.draw.line(bird_pic, black, (0,20),(10,30),3)
pg.draw.line(bird_pic, black, (0,10),(10,30),3)
pg.draw.line(bird_pic, black, (0,0),(10,30),3)
pg.draw.ellipse(bird_pic, red, (10,0,75,60))
pg.draw.ellipse(bird_pic, white, (50,5,20,20))
pg.draw.ellipse(bird_pic, black, (60,15,5,5))
pg.draw.ellipse(bird_pic, black, (35,30,35,15),2)
pg.display.flip()

#background
bg = pg.image.load("Flappy Background.png")

pipe_speed = -10
bird_speed = 8

#game variables
gap = 200

while True:
    #reset game
    top_pipe = pg.Rect(600,0,100,200)
    bottom_pipe = pg.Rect(600,425,100,175)
    bird = pg.Rect(100,200, 70, 50)

    play = 1
    score = 0

    while play == 1:
        pg.event.pump()

        #Updates
        top_pipe[0] += pipe_speed
        bottom_pipe[0] += pipe_speed
        bird[1] += bird_speed

        #Inputs
        L,M,R = pg.mouse.get_pressed()
        mx, my = pg.mouse.get_pos()

        #Events
        if top_pipe[0] <=0:
            top_pipe[0] = 800
            bottom_pipe[0] = 800
            score += 1

            #random pipe sizes
            top_pipe[3] = random.randint(100,400)
            bottom_pipe[1] = top_pipe[3] + gap
            bottom_pipe[3] = 600 - top_pipe[3] - gap

        if L== 1:
            bird[1] += -12

        if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
            play = 0

        #Drawing
        screen.blit(bg, (0,0))

        pg.draw.rect(screen, green,top_pipe)
        pg.draw.rect(screen, black,top_pipe,2)
        pg.draw.rect(screen, green,bottom_pipe)
        pg.draw.rect(screen, black,bottom_pipe,2)

        screen.blit(bird_pic, (bird[0],bird[1]))

        ex.printText(screen, black, score, 10, 10, 50)
        pg.display.flip()

        clock.tick(60)

    while R == 0:
        pg.event.pump()

        L,M,R = pg.mouse.get_pressed()

        screen.fill(white)
        ex.printText(screen, black, "Game Over", 50, 175, 150)
        ex.printText(screen, black, "Right Click to Continue", 60, 350, 70)
        pg.display.flip()
