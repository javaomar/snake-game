# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initialize game variables
game_is_on = True

# Main game loop
while game_is_on:
    screen.update()  # Update the screen manually
    time.sleep(0.2)  # Add a small delay to control the game speed
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset()
        
    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset_score()
            snake.reset()

# Keep the game window open until the user clicks
screen.exitonclick()
