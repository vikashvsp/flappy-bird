import pygame, sys

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,700))
    screen.blit(floor_surface,(floor_x_pos+576,700))

pygame.init()
screen=pygame.display.set_mode((576,840))
clock=pygame.time.Clock()

gravity=0.25
bird_movement=0

bg_surface=pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())

floor_surface=pygame.image.load('assets/base.png').convert()
floor_surface=pygame.transform.scale2x(floor_surface)
floor_x_pos=0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_surface=pygame.transform.scale2x(bird_surface)
bird_rect=bird_surface.get_rect(center=(100,350))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_movement=0
                bird_movement-=12
    screen.blit(bg_surface,(0,-150))

    bird_movement+=gravity
    bird_rect.centery+=bird_movement

    screen.blit(bird_surface,bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos<=-576:
        floor_x_pos=0
    pygame.display.update()
    clock.tick(120)