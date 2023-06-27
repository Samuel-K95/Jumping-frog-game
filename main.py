import pygame
import math
import random
from pygame import mixer


pygame.init()

screen = pygame.display.set_mode((1458, 943))

mixer.music.load('spring-weather-1.wav')
mixer.music.play(-1)

score=0


#background
back=pygame.image.load('finalpond.png')

 
#rocks
rocks=[]
rocksX=[]
rocksY=[]
num_of_rocks=5
for i in range(num_of_rocks):
    rocks.append(pygame.image.load('cave.png'))
    rocksX.append(random.randint(50, 1400))
    rocksY.append(random.randint(450, 500))

#flies
num_of_flies=3
fly= []
flyX=[]
flyY=[]
flyX_change=[]
for i in range(num_of_flies):
    fly.append(pygame.image.load('fly.png')) 
    flyX.append(1400)
    flyY.append(random.randint(100, 500))
    flyX_change.append(2)



#frog
frog= pygame.image.load('frog.png')
frogX=200
initialX=frogX
frogY=250
initialY=frogY
frogX_change=1
first=frogX_change
frogY_change=4
second= frogY_change

frog_life=5
frog_font=pygame.font.Font('freesansbold.ttf', 50)
frogfontX=1000
frogfontY=10

def showFlyLife(x, y):
    life=frog_font.render("life: " + str(frog_life), True, (255,255,255))
    screen.blit(life, (x, y))
#distance checker

def distance(x1,x2,y1, y2 ):
    distance = math.sqrt((math.pow((x2-x1),2))+ (math.pow((y2-y1), 2)))
    return distance

#score
score_value=0
font =pygame.font.Font('freesansbold.ttf', 50)
textX =10
textY= 10

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score, (textX, textY))



#Game over text
over_font =pygame.font.Font('freesansbold.ttf', 100)
def game_over_text():
    over_text=over_font.render("GAME OVER!!!!", True, (0,0,0))
    screen.blit(over_text, (400, 500))
    


#game loop


running= True 

while running:
    case=False
    flag=False
    screen.fill((0,0,0))

 
    screen.blit(back, (0,0))





    for i in range(num_of_rocks):
        screen.blit(rocks[i], (rocksX[i],rocksY[i]))
        #check if the frog is on the rock or not
        if distance(frogX,rocksX[i], frogY, rocksY[i])<30:
            frogX_change=0
            frogY_change=0
            case=True
            pos=i


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                frogY_change=-frogY_change
                second= -second
                jumping_sound= mixer.Sound('jump.wav')
                jumping_sound.play()
            if case:
                ribbet=mixer.Sound('frog-ribbet1.wav')
                ribbet.play()
                if event.key == pygame.K_j:
                    flag=True
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_SPACE:
                frogY_change *= -1
                second*=-1
                
                
    if flag:
        i=pos
        frogX_change= first
        if second<0:
            frogY_change =-1*second
        else:
            frogY_change= second
        rocksX[i], rocksY[i]= random.randint(50, 1400), random.randint(500, 550)

        score_value+=1
    
    
    screen.blit(frog, (frogX, frogY))
    if score_value%10==0 and score_value!=0:
        for i in range(num_of_flies):
            screen.blit(fly[i], (flyX[i], flyY[i]))  
            flyX[i]-=flyX_change[i] 
            if distance(frogX,flyX[i], frogY, flyY[i]) <= 50:
                frog_life+=1
                flyX[i]=10000
                flyY[i]=10000
                sparkle=mixer.Sound('Sparkle-sound-effect.wav')
                sparkle.play()
        

    frogX += frogX_change
    frogY += frogY_change
    if frogY>700:
        frog_life-=1
        frogX=initialX
        frogY=initialY
        splash=mixer.Sound('splash.wav')
        splash.play()
    if frogX>1450:
        frogX=12
     
    if frog_life<=0:
        game_over_text()
        frog_life=0
        for i in range(num_of_rocks):
            rocksX[i]=10000
            rocksY[i]=10000
            frogX=10000
            frogY=10000

            


    showFlyLife(frogfontX, frogfontY)
    show_score(textX, textY)            
    pygame.display.update()