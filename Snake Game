import turtle
import random

# screen constants
height = 700
width = 700
delay = 400  # Milliseconds
difficulty = turtle.textinput("Difficulty", "Enter Difficulty: Easy, Medium or Hard")
food_size = 10


def game_difficutly(difficulty):
    if (difficulty == 'Easy'):
        delay = 100
    elif (difficulty == 'Medium'):
        delay = 70
    elif (difficulty == 'Hard'):
        delay = 30
    else:
        delay = 100
    return delay


offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    screen.onkey(lambda: set_snake_direction("left"), "Left")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":  # No Self collision by pressing wrong key
            snake_direction = "up"
    elif direction == "right":
        if snake_direction != "left":  # No Self collision by pressing wrong key
            snake_direction = "right"
    elif direction == "down":
        if snake_direction != "up":  # No Self collision by pressing wrong key
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":  # No Self collision by pressing wrong key
            snake_direction = "left"


def game_loop():
    stamper.clearstamps()  # removes existing stamps

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check Collisions
    if new_head in snake or new_head[0] < - width / 2 or new_head[0] > width / 2 \
            or new_head[1] < - height / 2 or new_head[1] > height / 2:
        reset()
    else:
        # add head to snake body
        snake.append(new_head)

        # check food collision

        if not food_collision():
            # Remove last segment of snake
            snake.pop(0)  # Keep snake same length unless fed

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.title(f"Snake Game. Score: {score}")
        screen.update()
        turtle.ontimer(game_loop, game_difficutly(difficulty))


def food_collision():
    global food_pos, score
    if get_distance(snake[1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- width / 2 + food_size, width / 2 - food_size)
    y = random.randint(- height / 2 + food_size, height / 2 - food_size)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoran Theorem
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    # create snake as a list of coordinate pairs
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


# setup screen

screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake Game")
screen.bgcolor("light green")
screen.tracer(0)  # disables auto animation

# Event Handlers
screen.listen()
bind_direction_keys()

# create the stamper
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()

# set animation in motion
reset()

turtle.done()
