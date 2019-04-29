import pygame
from random import randint

BLOCK_SIZE = 10

class Color:
    def __init__(self):
        self.black = [0,0,0]
        self.red = [255,0,0]
        self.green = [0,255,0]
        self.blue = [0,0,255]

class Food:
    def __init__(self):
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE
        self.food = pygame.Rect(randint(1, 599), randint(1, 599), self.height, self.width)


class Player:
    def __init__(self):
        self.x, self.y = randint(20, 580), randint(20, 580)
        self.speed = 1
        self.blocks = 1
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE
        self.snake_positions = [pygame.Rect(self.x, self.y, self.height, self.width),
                                pygame.Rect(self.x - 10, self.y, self.height, self.width),
                                pygame.Rect(self.x - 20, self.y, self.height, self.width),
                                pygame.Rect(self.x - 30, self.y, self.height, self.width)]
        self.snake_head = self.snake_positions[0]
        #self.snake = pygame.Rect(self.x, self.y, self.height, self.width)
        self.score = 0
        self.direction = R


    def __len__(self):
        return self.blocks

    def check_position(self):
        if self.snake_head.bottom > 600:
            self.snake_head.top = 0
        elif self.snake_head.top < 0:
            self.snake_head.bottom = 600
        elif self.snake_head.left < 0:
            self.snake_head.right = 600
        elif self.snake_head.right > 600:
            self.snake_head.left = 0

    def set_direction(self, new_direction):
        direction = (0,0)
        if new_direction == R:
            direction = (self.speed,0)

        elif new_direction == L:
            direction = (-self.speed, 0)

        elif new_direction == U:
            direction = (0,-self.speed)

        elif new_direction == D:
            direction = (0, self.speed)

        center = 0,0
        for index, rect in enumerate(self.snake_positions):
            rect.move_ip(direction)

        #self.snake.move_ip(direction)

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def increase_speed(self):
        self.speed += .25

class Game:
    def __init__(self):
        pygame.display.set_caption('Dennis Snake Game')
        self.window_resolution = [600, 600]
        self.game_window = pygame.display.set_mode(self.window_resolution)
        self.start_time = pygame.time.Clock()
        self.colors = Color()
        self.snake = None
        self.food = None
        self.current_move = R
        self.init_new_game_window()

    def init_new_game_window(self):
        self.game_window.fill(self.colors.black)
        self.snake = Player()
        self.food = Food()
        pygame.display.update()

    def update_window(self):
        self.game_window.fill(self.colors.black)
        pygame.draw.rect(self.game_window, self.colors.red, self.food.food)
        # pygame.draw.rect(self.game_window, self.colors.green, self.snake.snake, 2)
        for rect in self.snake.snake_positions:
            pygame.draw.rect(self.game_window, self.colors.green, rect, 2)
        pygame.display.update()

    def check_for_eat_event(self):
        if self.snake.snake_head.colliderect(self.food.food):
            self.food = Food()
            self.snake.increment_score()
            print("Current Score: %d" % self.snake.score)
            if self.snake.get_score() % 10 == 0:
                self.snake.increase_speed()
    def start(self):
        while True:
            # clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and self.current_move != U:
                        self.current_move = D
                    if event.key == pygame.K_UP and self.current_move != D:
                        self.current_move = U
                    if event.key == pygame.K_LEFT and self.current_move != R:
                        self.current_move = L
                    if event.key == pygame.K_RIGHT and self.current_move != L:
                        self.current_move = R
            print(self.snake.speed)
            self.check_for_eat_event()
            self.snake.check_position()
            self.snake.set_direction(self.current_move)
            self.update_window()



if __name__ == '__main__':

    pygame.init()
    game = Game()
    game.start()



