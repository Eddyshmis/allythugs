import sys
import pygame
import classes
width = 1200
height = 800
center_x = (width/2)
center_y = (height/2)
start_game = False
menu_screen = True
faded_in = False
pygame.init()
pygame.mixer.init()
pygame.joystick.init()

pygame.display.set_caption("AllyThugs")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
start_bt_img = pygame.image.load("start_retro.png")
start_bt = classes.Button(440,320,start_bt_img,5)


#transformed image
foreground_image = pygame.image.load("cyberpunk-street-files\cyberpunk-street-files\Version 1\PNG\layers\\foreground.png").convert_alpha()
# background_transform = pygame.transform.scale(background_image,(1000,100))
back_buildings_image = pygame.image.load("cyberpunk-street-files\cyberpunk-street-files\Version 1\PNG\layers\\back-buildings.png").convert_alpha()
far_buildings_image = pygame.image.load("cyberpunk-street-files\cyberpunk-street-files\Version 1\PNG\layers\\far-buildings.png").convert_alpha()

first_man_image = pygame.image.load("first_man.png")
first_man = classes.Player(0,0,first_man_image,2)

foreground = classes.image(0,0,foreground_image,4.5)
foreground_1 = classes.image(1584,0,foreground_image,4.5)

back_buildings = classes.image(15,0,back_buildings_image,4.5)
back_buildings_1 = classes.image(1197,0,back_buildings_image,4.5)

far_buildings = classes.image(15,0,far_buildings_image,5)
far_buildings_1 = classes.image(1197,0,far_buildings_image,5)

background_music = pygame.mixer.Sound("cyberpunk-street-files\cyberpunk-street-files\music\cyberpunk-street.mp3")
music_playing = False



def loadBackground():
    far_buildings.draw(screen)
    far_buildings_1.draw(screen)

    back_buildings.draw(screen)
    back_buildings_1.draw(screen)

    foreground.draw(screen)
    foreground_1.draw(screen)

    foreground.rect.centerx -= 3
    foreground_1.rect.centerx -= 3 
    
    back_buildings.rect.centerx -= 2
    back_buildings_1.rect.centerx -= 2

    far_buildings.rect.centerx -= 1
    far_buildings_1.rect.centerx -= 1
    
    if foreground.rect.centerx <= -792:
        foreground.rect.centerx = 792
        foreground_1.rect.centerx = 2376
    if back_buildings.rect.centerx <= -591:
        back_buildings.rect.centerx = 591
        back_buildings_1.rect.centerx = 1773
    if far_buildings.rect.centerx <= -591:
        far_buildings.rect.centerx = 591
        far_buildings_1.rect.centerx = 1773
def fade_screen_black():
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    for alpha in range(0,300,1):
        fade.set_alpha(alpha)
        screen.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(10)
def loading_screen(func):
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    for alpha in range(300,0,-1):
        fade.set_alpha(alpha)
        func()
        screen.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(10)
def gameLogic():
    print("start")

while True:
    if not music_playing:
        background_music.play(1)
        background_music.set_volume(0.1)
        music_playing = True
        print("music")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    while menu_screen:
        #play game
        screen.fill((0,0,0))
        loadBackground()
        if start_bt.draw(screen):
            start_game = True
            print("pressed")
            break
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(event)
            if event.type == pygame.JOYAXISMOTION:
                print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(back_buildings.rect.centerx)
        pygame.display.update()
        pygame.time.delay(10)
    while start_game:
        if faded_in == False:
            fade_screen_black()
            faded_in = True
        # loading_screen(loadBackground)
        first_man.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        pygame.display.update()
    clock.tick(60)
    pygame.display.update()