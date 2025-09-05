import pygame
# Initialiize required moduls
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400, 500))

# Create a loop to run till the game is quit by the user
done = False
# Load and scale images directly

penguin_image = pygame.transform.scale(
    pygame.image.load('hello penguin.jpg').convert_alpha(), (500, 800)
)
penguin_rect = penguin_image.get_rect(center=(400 // 2,
                                              300 // 2 - 30))

# Initialize font, render text, and set text position
text = pygame.font.Font(None, 36).render('Hello World ', True,
                                         pygame.Color('black'))

text_rect = text.get_rect(center=(400 // 2, 300 // 2 + 110))
while not done:
    # Clear the event queue
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(penguin_image,penguin_rect)
    screen.blit(text, text_rect)
    # Make the changes visible

    pygame.display.flip()
