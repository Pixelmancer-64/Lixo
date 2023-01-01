import random
import math
from PIL import Image

def generate_color():
    r = random.randint(0, 32)
    g = random.randint(0, 32)
    b = random.randint(0, 32)
    return (r * 8, g * 8, b * 8)

def create_algorithmic_image(size):
    image = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == size // 2 and j == size // 2:
                row.append((255, 255, 255))
            else:
                # Calculate distance from center
                distance = math.sqrt((size // 2 - i) ** 2 + (size // 2 - j) ** 2)
                # Generate color based on distance
                pixel = (int(distance * 8), int(distance * 8), int(distance * 8))
                row.append(pixel)
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
    image = create_algorithmic_image(size)
    save_image(image, 'algorithmic_image.png')

main()
