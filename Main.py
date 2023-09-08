import sys
import pygame
import classes
width = 1200
height = 800
center_x = (width/2)
center_y = (height/2)
start_game = False

pygame.init()
pygame.mixer.init()
pygame.joystick.init()

pygame.display.set_caption("AllyThugs")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
start_bt_img = pygame.image.load("start.png")
start_bt = classes.Button((center_x - 400),(center_y - 250),start_bt_img,0.5)


#transformed image
foreground_image = pygame.image.load("cyberpunk-street-files\cyberpunk-street-files\Version 1\PNG\layers\\foreground.png").convert_alpha()
# background_transform = pygame.transform.scale(background_image,(1000,100))
back_buildings_image = pygame.image.load("cyberpunk-street-files\cyberpunk-street-files\Version 1\PNG\layers\\back-buildings.png").convert_alpha()
far_buildings_image = pygame.image.load("cyberpunk-street-files\cyberpunk-street-files\Version 1\PNG\layers\\far-buildings.png").convert_alpha()
foreground = classes.image(0,0,foreground_image,4.5)
back_buildings = classes.image(0,0,back_buildings_image,4.5)
far_buildings = classes.image(0,0,far_buildings_image,5)

background_music = pygame.mixer.Sound("cyberpunk-street-files\cyberpunk-street-files\music\cyberpunk-street.mp3")
music_playing = False
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
    if start_bt.draw(screen):
        start_game = True
    while start_game:
        #play game
        screen.fill((0,0,0))
        # screen.blit(background_transform,(0,0))
        far_buildings.draw(screen)
        back_buildings.draw(screen)
        foreground.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(event)
            if event.type == pygame.JOYAXISMOTION:
                print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
    clock.tick(60)
    pygame.display.update()