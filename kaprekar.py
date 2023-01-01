# import pygame

# # Constants
# KAPREKAR_CONSTANT = 6174
# GRID_WIDTH = 4
# GRID_HEIGHT = 4

# # Initialize Pygame
# pygame.init()
# font = pygame.font.Font('freesansbold.ttf', 32)

# # Set the window size
# window_size = (800, 600)

# # Create the window
# screen = pygame.display.set_mode(window_size)

# # Set the title of the window
# pygame.display.set_caption("Kaprekar Constant")

# # Set the background color
# screen.fill((0, 0, 0))

# # Set the cell size
# cell_size = window_size[0] // GRID_WIDTH

# # Set the colors
# colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# # Set the current number
# current_number = 0

# # Set the current position
# current_position = (0, 0)

# # Set the running flag to True
# running = True

# # Run the game loop
# while running:
#     # Process events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Draw the current number
#     text_surface = font.render(str(current_number), True, colors[current_number % 3])
#     screen.blit(text_surface, (current_position[0] * cell_size, current_position[1] * cell_size))

#     # Update the current position
#     current_position = (current_position[0] + 1, current_position[1])
#     if current_position[0] >= GRID_WIDTH:
#         current_position = (0, current_position[1] + 1)
#     if current_position[1] >= GRID_HEIGHT:
#         current_position = (0, 0)

#     # Update the current number
#     current_number = (current_number + KAPREKAR_CONSTANT) % 10000

#     # Update the display
#     pygame.display.update()

# # Quit Pygame
# pygame.quit()










import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Kaprekar Constant")

# Set the number of rows and columns in the grid
rows = 50
cols = 50

# Set the size of each cell in the grid
cell_size = (window_size[0] // cols, window_size[1] // rows)

# Set the Kaprekar constant
kaprekar_constant = 6174

# Set the maximum number of steps to reach the Kaprekar constant
max_steps = 100

# Set the color range for the cells
color_range = (0, 255)

# Create a list to store the colors for each step
colors = []
for i in range(max_steps):
    # Generate a random color for each step
    r = random.uniform(color_range[0], color_range[1])
    g = random.uniform(color_range[0], color_range[1])
    b = random.uniform(color_range[0], color_range[1])
    color = (r, g, b)
    colors.append(color)

# Create a 2D array to store the grid
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Set the running flag to True
running = True

# Run the game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Loop through the rows and columns in the grid
    for row in range(rows):
        for col in range(cols):
            # Calculate the number of steps required to reach the Kaprekar constant or 0
            number = row * cols + col
            steps = 0
            while number != kaprekar_constant and number != 0 and steps < max_steps:
                steps += 1
                number = sum(int(digit) for digit in str(number))

            # Assign a color to the cell based on the number of steps
            steps = steps % len(colors)
            print(steps)
            color = colors[steps]

            # Calculate the position of the cell
            x = col * cell_size[0]
            y = row * cell_size[1]

            # Draw the cell
            pygame.draw.rect(screen, color, (x, y, cell_size[0], cell_size[1]))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

