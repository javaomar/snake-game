# Import necessary modules
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Create the Scoreboard class to keep track of the player's score
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()  # Initialize scoreboard with score 0

    def update_scoreboard(self):
        # Update the scoreboard with the current score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Display "GAME OVER" message in the center of the screen
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Increase the score and update the scoreboard
        self.score += 1
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Update with the new score
