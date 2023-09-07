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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if start_bt.draw(screen):
        start_game = True
    while start_game:
        #play game
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(event)
            if event.type == pygame.JOYAXISMOTION:
                print(event)
    clock.tick(60)
    pygame.display.update()