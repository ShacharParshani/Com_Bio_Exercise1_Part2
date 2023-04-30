import time

import pygame

from Automaton import Automaton
from InputTextBox import InputTextBox

# Initialize Pygame
pygame.init()
automat = None

# Set up the display
screen_width = 700
screen_height = 700

# Set the dimensions of the matrix
matrix_width = 100
matrix_height = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shachar & Liel")

# Define the font
font = pygame.font.SysFont('Arial', 16)

# Define the text boxes
p_text_box = InputTextBox("P: (between 0-1)", pygame.Rect(10, 30, 150, 30))
l_text_box = InputTextBox("L:", pygame.Rect(200, 30, 150, 30))
endGen_text_box = InputTextBox("endGen:", pygame.Rect(10, 240, 150, 30))

# Define the submit button
submit_button = pygame.Rect(200, 240, 150, 30)
submit_text = font.render("Submit", True, (100, 50, 80))

# Define the function to be executed when the submit button is clicked
def submit_function():
    global automat
    automat = Automaton(float(p_text_box.input_text),
                        float(l_text_box.input_text),
                        None,
                        None,
                        None,
                        None,
                        float(endGen_text_box.input_text))
    print(automat.p)

def draw_matrix():
    # Draw the matrix
    cell_size = 7
    for x in range(matrix_width):
        for y in range(matrix_height):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

            if automat.matrix[y][x] is None:
                pygame.draw.rect(screen, (0, 0, 0), rect, 0)
            elif automat.matrix[y][x].gen != -1:
                pygame.draw.rect(screen, (255, 192, 203), rect, 0)
            else:
                pygame.draw.rect(screen, (255, 255, 255), rect, 0)


# Define the game loop
running = True
initial_screen = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the submit button was clicked
            if submit_button.collidepoint(event.pos):
                submit_function()
                initial_screen = False
        elif event.type == pygame.KEYDOWN:
            # Check if a key was pressed while in the input box
            if p_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                p_text_box.GetPos(event, font, screen)

            if l_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                l_text_box.GetPos(event, font, screen)

            if endGen_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                endGen_text_box.GetPos(event, font, screen)
    # Fill the background
    screen.fill((255, 255, 255))

    if initial_screen:
        # Draw the text boxes
        p_text_box.Draw(font, screen, (10, 10))
        l_text_box.Draw(font, screen, (200, 10))
        endGen_text_box.Draw(font, screen, (10, 210))

        # Draw the submit button
        pygame.draw.rect(screen, (100, 50, 80), submit_button, 2)
        screen.blit(submit_text, (submit_button.x + 5, submit_button.y + 5))

        # Update the display
        pygame.display.update()

    else:

        # automat.create_matrix()
        automat.create_matrix()

        # Fill the background
        screen.fill((255, 255, 255))

        # Create the screen
        screen = pygame.display.set_mode((screen_width, screen_height))

        automat.random_starter()
        draw_matrix()
        pygame.display.update()
        time.sleep(0.5)

        automat.first_gen()
        draw_matrix()
        pygame.display.update()

        # Run the matrix loop
        while automat.generation <= automat.endGen:
            automat.gen_running()
            draw_matrix()
            pygame.display.update()
            time.sleep(0.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        time.sleep(30)
        running = False




