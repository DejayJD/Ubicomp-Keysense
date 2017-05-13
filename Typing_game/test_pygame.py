import sys, pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Moving Box")


clock = pygame.time.Clock()
font = pygame.font.SysFont('Adobe Arabic', 32)



box_x = 300
box_dir = 3

text = "Type Here: "

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.name(event.key)
            if (key_pressed == "space"):
                key_pressed = " "
            if (key_pressed == "return"):
                key_pressed = "\n"
            text += key_pressed
            if event.key == 27:
                sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()

    label = font.render(text, 1, (255, 255, 0))
    screen.blit(label, (0, 0))

    clock.tick(60)
    pygame.display.flip()

