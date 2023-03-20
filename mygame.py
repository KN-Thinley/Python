import pygame, sys, random
title = 'The Ultimate Pong Game'
pygame.display.set_caption(title) 
    
def playermation():
    player.y += player_speed
    
    if player.top <= 0 :
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height
    

def oppomation():
    if opponent.top < pong.y :
        opponent.top += opponent_speed
    if opponent.bottom >= pong.y :
        opponent.bottom -= opponent_speed 
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height :
        opponent.bottom = screen_height

def pong_restart():
    global pong_speed_x, pong_speed_y
    pong.center = (screen_width/2, screen_height/2)
    pong_speed_y *= random.choice((1, -1))
    pong_speed_x *= random.choice((1, -1))
    
def pongmation() :
    global pong_speed_x , pong_speed_y
    pong.x += pong_speed_x
    pong.y += pong_speed_y 
        
    if pong.top <= 0 or pong.bottom >= screen_height:
        pong_speed_y *= -1

    if pong.left <= 0 or pong.right >= screen_width:
        pong_restart()
        
    if pong.colliderect(player) or pong.colliderect(opponent):
        pong_speed_x *= -1
        pong_speed_y *= -1

        
pygame.init()
clock = pygame.time.Clock()
scoreA =0
scoreB = 0
screen_width = 1280
screen_height = 720  
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 74)
pong = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width -20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10 ,140)

backcolor = pygame.Color('darkblue')
red = (255,0,0)
white = (255,255,255)
orange = pygame.Color('darkorange')

pong_speed_x = 8 * random.choice((1,-1))
pong_speed_y = 8 * random.choice((1,-1))
player_speed = 0
opponent_speed = 8

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP :
                player_speed -= 7
        if event.type == pygame.KEYUP:             
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP :
                player_speed += 7
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_s :
                opponent_speed  -= 7
            if event.key == pygame.K_w :
                opponent_speed += 7
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_s :
                opponent_speed  -= 7
            if event.key == pygame.K_w :
                opponent_speed += 7
        

    screen.fill(backcolor)
    pygame.draw.rect(screen, red , player)
    pygame.draw.rect(screen,red, opponent)
    pygame.draw.ellipse(screen, orange , pong) 
    pygame.draw.line(screen, white, (screen_width/2,0), (screen_width/2, screen_height ))
    pygame.draw.aaline(screen, white, (screen_width/2.01,0), (screen_width/2.01, screen_height))
    pygame.draw.aaline(screen, white, (0,screen_height/2,), (screen_width, screen_height/2,))
    
    text = font.render('SCORE', 1 ,(10, 10 ,10), white)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    screen.blit(text, textpos)
    
    def scoreforA() :
        text = font.render(str(scoreA), 400, white)
        screen.blit(text, (250, 10))
    def scoreforB(): 
        text = font.render(str(scoreB), 400, white)
        screen.blit(text, (420,10))
    def score() :
        if pong.left <= 0 :
            score_opponent += scoreforA()
            text = font.render(str(score_opponent, 400, white))
            screen.blit(text,(420, 10))
        if pong.right >= screen_width:
            score_player += scoreforB()
            text = font.render(str(score_player(),400, white))
            screen.blit(text,(420, 10))
    scoreforA()
    scoreforB()
    score()
    pongmation()
    playermation()
    oppomation()
    
    pygame.display.flip()
    clock.tick(60)


