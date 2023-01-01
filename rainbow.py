import random
import math
from PIL import Image

def generate_color(neighbors):
    # Generate a random color
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    color = (r, g, b)

    # Modify the color based on the neighbors
    for neighbor in neighbors:
        r_diff = abs(color[0] - neighbor[0])
        g_diff = abs(color[1] - neighbor[1])
        b_diff = abs(color[2] - neighbor[2])
        total_diff = r_diff + g_diff + b_diff
        if total_diff > 256:
            return neighbor
    return color

def create_image(size):
    image = []
    for i in range(size):
        row = []
        for j in range(size):
            # Get the neighboring cells
            neighbors = []
            if i > 0:
                neighbors.append(image[i - 1][j])
            if j > 0:
                neighbors.append(row[j - 1])
            # Generate the color for this cell
            color = generate_color(neighbors)
            row.append(color)
        image.append(row)
    return image

def save_image(image, filename):
    # Create a new image with the given size
    img = Image.new('RGB', (len(image[0]), len(image)))

    # Iterate over the rows and columns of the image and set the pixel value
    for y in range(img.height):
        for x in range(img.width):
            img.putpixel((x, y), image[y][x])

    # Save the image to the specified file
    img.save(filename)

def main():
    size = 256
    image = create_image(size)
    save_image(image, 'algorithmic_image.png')

main()