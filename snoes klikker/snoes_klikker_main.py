import pgzrun
import random
import time
import os

WIDTH = 800
HEIGHT = 600

snoezen = 0
sps = 0
fabrieken_gekocht = 0
kantoren_gekocht = 0
steden_gekocht = 0
landen_gekocht = 0
planeten_gekocht = 0
stelsels_gekocht = 0

snoes = Actor('snoes')
snoes.pos = 150, 100

koop_fabriek = Actor('koop_fabriek')
koop_fabriek.pos = 125, 300

koop_kantoor = Actor('koop_kantoor')
koop_kantoor.pos = 350, 300

koop_stad = Actor('koop_stad')
koop_stad.pos = 575, 300

koop_land = Actor('koop_land')
koop_land.pos = 125, 425

koop_planeet = Actor('koop_planeet')
koop_planeet.pos = 350, 425

koop_stelsel= Actor('koop_stelsel')
koop_stelsel.pos = 575, 425

#music.play('track.wav')

def draw():
    global fabrieken_gekocht, kantoren_gekocht, steden_gekocht, landen_gekocht, planeten_gekocht, stelsels_gekocht
    screen.fill('grey')
    koop_fabriek.draw()
    koop_kantoor.draw()
    koop_stad.draw()
    koop_land.draw()
    koop_planeet.draw()
    koop_stelsel.draw()
    snoes.draw()
    screen.draw.text('Snoezen: ' + str(snoezen), (300, 100), color='black')
    screen.draw.text('Snoezen per seconde: ' + str(sps), (500, 100), color='black')

def on_mouse_down(pos):
    global snoezen, sps, fabrieken_gekocht, kantoren_gekocht
    if snoes.collidepoint(pos):
        snoezen += 1
    elif koop_fabriek.collidepoint(pos):
        if snoezen >= 50:
            snoezen -= 50
            sps += 1
            fabrieken_gekocht += 1
            os.system('afplay /System/Library/Sounds/Focus.aiff')
    elif koop_kantoor.collidepoint(pos):
        if snoezen >= 250:
            snoezen -= 250
            sps += 10
            kantoren_gekocht += 1
            os.system('afplay /System/Library/Sounds/Focus.aiff')
    elif koop_stad.collidepoint(pos):
        if snoezen >= 1500:
            snoezen -= 1500
            sps += 50
            steden_gekocht += 1
            os.system('afplay /System/Library/Sounds/Focus.aiff')
    elif koop_land.collidepoint(pos):
        if snoezen >= 15000:
            snoezen -= 15000
            sps += 200
            landen_gekocht += 1
            os.system('afplay /System/Library/Sounds/Focus.aiff')
    elif koop_planeet.collidepoint(pos):
        if snoezen >= 100000:
            snoezen -= 100000
            sps += 500
            planeten_gekocht += 1
            os.system('afplay /System/Library/Sounds/Focus.aiff')
    elif koop_stelsel.collidepoint(pos):
        if snoezen >= 1000000:
            snoezen -= 1000000
            sps += 1000
            stelsels_gekocht += 1
            os.system('afplay /System/Library/Sounds/Focus.aiff')
    else:
        pass

def update_snoezen():
    global snoezen, fabrieken_gekocht, sps, kantoren_gekocht, steden_gekocht, landen_gekocht, planeten_gekocht, stelsels_gekocht
    sps = (fabrieken_gekocht * 1) + (kantoren_gekocht * 10) + (steden_gekocht * 50) + (landen_gekocht * 200) + (planeten_gekocht * 500) + (stelsels_gekocht * 1000) + 0
    snoezen += sps
    clock.schedule(update_snoezen, 1)

update_snoezen()
pgzrun.go()
