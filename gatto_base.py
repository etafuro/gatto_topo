"""
Eseguire da terminale con:

pgzrun gatto_base.py
"""

import random

# Dimensioni della finestra
WIDTH = 960
HEIGHT = 600

# Creo gli sprite
gatto = Actor("cat")
topo = Actor("mouse")

# Queste sono variabili: non esistono come proprietà di Actor
topo_speed_x = 1
topo_speed_y = -1

# Questa è una proprietà di Actor
topo.center = (random.randint(200, 700), random.randint(100, 500))


def draw():
    """
    Eseguita ad ogni frame per ridisegnare lo schermo.
    """

    screen.fill((255, 255, 255))  # sfondo bianco
    gatto.draw()
    topo.draw()


def update():
    """
    Eseguita ad ogni frame per aggiornare il gioco.

    Spiegare che questa è una differenza fondamentale rispetto a Scratch: qui occorre eseguire le animazioni e i controlli un passo alla volta. Non si possono gestire i cambiamenti come cicli "per sempre" perché bloccherebbero il gioco.
    """

    global topo_speed_x, topo_speed_y

    # sposto il topo di un solo passo
    topo.x = topo.x + topo_speed_x
    topo.y = topo.y + topo_speed_y

    # controllo bordi
    if (topo.top <=0) or (topo.right >= WIDTH) or (topo.bottom >= HEIGHT) or (topo.left <=0):
        # inverto la velocità per non farlo uscire. Se esce mi dà problemi nel chiamare topo_reset() per reimpostare la posizione
        topo_speed_x = -1 * topo_speed_x
        topo_speed_y = -1 * topo_speed_y


    # controllo la collisione
    if gatto.colliderect(topo):
        sounds.splat.play()
        # trucco per rimuovere temporaneamente il topo dal gioco: lo sposto fuori dalla finestra
        topo.center = (-100, -100)
        clock.schedule_unique(topo_reset, 4.0)


def topo_reset():
    """
    Ripristina il topo in una posizione casuale e con direzione di moto casuale.
    """

    global topo_speed_x, topo_speed_y

    # l'espressione più comoda per ottenere a caso 1 o -1 sarebbe [-1,1][random.randrange(2)]
    # ma è complicata da spiegare.
    # Usiamo randint che già utilizziamo per il centro, anche se include il valore zero.
    topo_speed_x = random.randint(-1,1)
    topo_speed_y = random.randint(-1,1)
    topo.center = (random.randint(200, 700), random.randint(100, 500))


def on_mouse_move(pos):
    """
    Gira e muove il gatto verso la posizione del mouse.
    """

    gatto.angle = gatto.angle_to(pos)
    animate(gatto, pos=pos)

