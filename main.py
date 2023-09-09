#!/usr/bin/pgzrun

import pygame

WIDTH=540
HEIGHT=960

note_green = Actor('note_green')
note_green.pos = 100,56
music.play('music.mp3')

def draw():
  screen.fill((255,255,255))
  note_green.draw()

def update():
  mouse_pos = pygame.mouse.get_pos()
  if note_green.collidepoint(mouse_pos):
    print("Work")