import pgzrun, random

TITLE="Cat and Hamster"
WIDTH=400
HEIGHT=400
score=0

cat=Actor("cat")
cat.pos=80,90

hamster=Actor("hamster")
hamster.pos=240,250

def draw():
    global score
    screen.blit('background',(0,0))
    cat.draw()
    hamster.draw()
    screen.draw.text("Score: "+str(score), color="brown", topright=(280,30))


def update():
    global score
    if keyboard.left:
        cat.x-=5
    if keyboard.right:
        cat.x+=5
    if keyboard.up:
        cat.y-=5
    if keyboard.down:
        cat.y+=5
    colliding=cat.colliderect(hamster)
    if colliding:
        hamster.x=random.randint(40,280)
        hamster.y=random.randint(40,280)
        score+=5


pgzrun.go()