# Import necessary modules
from turtle import Turtle
import random

# Create the Food class, which represents the snake's food
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # Initialize food position

    def refresh(self):
        # Move the food to a random position within the screen boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
