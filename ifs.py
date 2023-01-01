# import turtle
# import random

# # Set the number of transformations
# n_transformations = 3

# # Set the probability of applying each transformation
# probabilities = [0.5, 0.3, 0.2]

# # Set the probability threshold for each transformation
# thresholds = [0.5, 0.8, 1.0]

# # Set the transformation matrices
# transformations = [
#     [[0.5, 0.0], [0.0, 0.5]],
#     [[0.5, 0.0], [0.0, 0.5]],
#     [[0.5, 0.0], [0.0, 0.5]]
# ]

# # Set the starting point
# x = 0
# y = 0

# # Set the pen size and color
# turtle.pensize(1)
# turtle.colormode(255)
# turtle.pencolor(0,0,0)

# # Set the number of points to draw
# n_points = 100000

# # Draw the points
# for i in range(n_points):
#     # Choose a transformation at random
#     r = random.random()
#     for j in range(n_transformations):
#         if r < thresholds[j]:
#             # Apply the transformation
#             x_new = x * transformations[j][0][0] + y * transformations[j][0][1]
#             y_new = x * transformations[j][1][0] + y * transformations[j][1][1]
#             x = x_new
#             y = y_new
#             break
#     # Draw the point
#     turtle.goto(x, y)
#     turtle.dot()

# # Show the window
# turtle.done()


import turtle
import random

# Initialize the turtle
turtle.tracer(0, 0)
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)

# Set the window size
window_size = (800, 600)

# Set the number of iterations to perform
iterations = 10000

# Set the IFS probability distribution
prob_dist = [(0.2, 0.0, 0.0, 0.2, 0.0, 0.0),
             (0.2, 0.0, 0.0, 0.2, 0.5, 0.5),
             (0.0, 0.2, 0.0, 0.0, 0.5, 0.0)]

# Set the starting position and heading
x = 0
y = 0
heading = 0

# Set the color range for the particles
color_range = (0, 255)

# Set the maximum size of the particles
max_size = 10

# Set the maximum speed of the particles
max_speed = 5

# Generate the IFS fractal
for i in range(iterations):
    # Choose a random transformation
    t = random.choices(prob_dist, weights=[0.3, 0.3, 0.4])[0]

    # Apply the transformation
    x, y = t[0]*x + t[1]*y + t[4], t[2]*x + t[3]*y + t[5]
    heading += t[5]

    # Generate a random size for the particle
    size = random.uniform(1, max_size)

    # Generate a random velocity for the particle
    vx = random.uniform(-max_speed, max_speed)
    vy = random.uniform(-max_speed, max_speed)

    # Generate a random color for the particle
    r = random.uniform(color_range[0], color_range[1])
    g = random.uniform(color_range[0], color_range[1])
    b = random.uniform(color_range[0], color_range[1])
    color = turtle.color(int(r), int(g), int(b))

    # Set the pen color
    turtle.pencolor(color)

    # Draw the particle
    turtle.setpos(x, y)
    turtle.dot(size)

# Update the screen
turtle.update()

# Keep the window open
turtle.mainloop()
