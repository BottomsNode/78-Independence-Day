import turtle
import pygame
from pygame import mixer
import time  

# Initialize pygame mixer
pygame.init()
mixer.init()

# Load and play background music
mixer.music.load('./song.mp3')  # Replace with the path to your music file
mixer.music.play()  # Play the music once

# Defining the Output Source Which is our Screen
screen = turtle.Screen()
screen.title("Indian Flag Animation")
screen.setup(width=800, height=550)
screen.tracer(0)  # Disable automatic screen updates

t = turtle.Turtle()
t.speed(0)  # Set turtle speed to the maximum, we'll manually control the delay

# Draw the Text Above the Flag
def draw_text(message, position, font_size, color):
    t.penup()
    t.goto(position)
    t.color(color)
    t.pendown()
    t.write(message, align="center", font=("Arial", font_size, "bold"))
    screen.update()
    time.sleep(1)  # Add a delay to slow down the drawing

draw_text("Har Screen Tiranga", (0, 200), 30, "black")
draw_text("Happy Independence Day 2024", (0, 140), 25, "black")

# Initially penup()
t.penup()
t.goto(-200, 125)
t.pendown()

# Indian Flag Color (ORANGE)
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(84)
screen.update()
time.sleep(1)  # Add a delay to make the drawing visible

# Indian Flag Color (GREEN)
t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.end_fill()
screen.update()
time.sleep(1)  # Add a delay to make the drawing visible

# Ashoka Chakra
t.penup()
t.goto(35, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()
screen.update()
time.sleep(1)  # Add a delay to make the drawing visible

t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()
screen.update()
time.sleep(1)  # Add a delay to make the drawing visible

t.penup()
t.goto(-27, -4)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.forward(7)
    t.right(15)
    t.pendown()
    screen.update()
    time.sleep(0.1)  # Add a delay for each spoke

# The Ashoka Chakra of the Flag
t.color("navy")
t.penup()
t.goto(10, 0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
screen.update()
time.sleep(1)  # Add a delay to make the drawing visible

# Spokes Of the Chakra
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)
    screen.update()
    time.sleep(0.1)  # Add a delay for each spoke

# Draw the Text Below the Flag
draw_text("Wishes By Nishit Shivdasani", (0, -180), 18, "black")

# Complete the drawing
t.hideturtle()
turtle.done()
pygame.quit()