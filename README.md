# Brick Breaker Game

This is a simple Brick Breaker game implemented using Pygame.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install Pygame using pip:
    ```sh
    pip install pygame
    ```

## How to Run

1. Clone this repository or download the [py3.py](http://_vscodecontentref_/0) file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing [py3.py](http://_vscodecontentref_/1).
4. Run the game using the following command:
    ```sh
    python py3.py
    ```

## Game Controls

- Use the left arrow key (`←`) to move the paddle left.
- Use the right arrow key (`→`) to move the paddle right.

## Game Rules

- The ball will bounce off the walls, paddle, and bricks.
- The game resets if the ball hits the bottom of the screen.
- Destroy bricks by hitting them with the ball.
- Occasionally, a power-up will drop from a destroyed brick.
- Catch the power-up with the paddle to increase the paddle size.

## Code Overview

- [WIDTH](http://_vscodecontentref_/2), [HEIGHT](http://_vscodecontentref_/3): Screen dimensions.
- [WHITE](http://_vscodecontentref_/4), [BLACK](http://_vscodecontentref_/5), [RED](http://_vscodecontentref_/6), [GREEN](http://_vscodecontentref_/7), [BLUE](http://_vscodecontentref_/8), [YELLOW](http://_vscodecontentref_/9): Color definitions.
- [ball_radius](http://_vscodecontentref_/10), [ball_pos](http://_vscodecontentref_/11), [ball_vel](http://_vscodecontentref_/12): Ball properties.
- [paddle_width](http://_vscodecontentref_/13), [paddle_height](http://_vscodecontentref_/14), [paddle_pos](http://_vscodecontentref_/15), [paddle_speed](http://_vscodecontentref_/16): Paddle properties.
- [brick_width](http://_vscodecontentref_/17), [brick_height](http://_vscodecontentref_/18), [brick_rows](http://_vscodecontentref_/19), [brick_cols](http://_vscodecontentref_/20), [bricks](http://_vscodecontentref_/21): Brick properties.
- [power_up_size](http://_vscodecontentref_/22), [power_up_speed](http://_vscodecontentref_/23), [power_ups](http://_vscodecontentref_/24): Power-up properties.
- [clock](http://_vscodecontentref_/25), [FPS](http://_vscodecontentref_/26): Frame rate control.
