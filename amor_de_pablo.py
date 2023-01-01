import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("I LOVE YOU KAYLANE")

# Set the text to be displayed
text = "I LOVE YOU KAYLANE"

# Set the font and size
font = pygame.font.Font('freesansbold.ttf', 52, bold=True)

# Render the text as an image
text_image = font.render(text, True, (255, 255, 255))

# Get the size of the text image
text_image_size = text_image.get_size()

# Create a list to store the particles
particles = []

# Set the number of particles to create
num_particles = 1000

# Set the maximum size of the particles
max_size = 10

# Set the maximum speed of the particles
max_speed = .5

# Set the color range for the particles
color_range = (0, 255)

# Create the particles
for i in range(num_particles):
    # Generate a random size for the particle
    size = random.uniform(1, max_size)

    # Generate a random position for the particle
    x = random.uniform(0, window_size[0])
    y = random.uniform(0, window_size[1])

    # Generate a random velocity for the particle
    vx = random.uniform(-max_speed, max_speed)
    vy = random.uniform(-max_speed, max_speed)

    # Generate a random color for the particle
    r = random.uniform(color_range[0], color_range[1])
    g = random.uniform(color_range[0], color_range[1])
    b = random.uniform(color_range[0], color_range[1])
    color = (r, g, b)

    # Create the particle and add it to the list
    particle = (x, y, size, vx, vy, color)
    particles.append(particle)

# Set the running flag to True
# Set the running flag to True
running = True

# Run the game loop
while running:
    # Update the positions of the particles
    for i in range(num_particles):
        # Get the particle
        x, y, size, vx, vy, color = particles[i]

        # Update the particle's position
        x += vx
        y += vy

        # Check if the particle is off the screen
        if x < 0 or x > window_size[0] or y < 0 or y > window_size[1]:
            # If the particle is off the screen, generate a new random position for it
            x = random.uniform(0, window_size[0])
            y = random.uniform(0, window_size[1])

        # Update the particle in the list
        particles[i] = (x, y, size, vx, vy, color)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the particles
    for particle in particles:
        x, y, size, vx, vy, color = particle
        pygame.draw.circle(screen, color, (int(x), int(y)), int(size))

    # Draw the text image
    screen.blit(text_image, (window_size[0] / 2 - text_image_size[0] / 2, window_size[1] / 2 - text_image_size[1] / 2))

    # Update the display
    pygame.display.flip()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
