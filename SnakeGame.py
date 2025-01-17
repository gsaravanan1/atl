class SnakeGame:
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        self.snake = [(0, 0)]

    def move(self, direction):
        head = self.snake[0]
        tail = self.snake[-1]

        # Pop the tail, as the snake moves forward
        self.snake.pop()

        if direction == 'U':
            head = (head[0] - 1, head[1])
        elif direction == 'L':
            head = (head[0], head[1] - 1)
        elif direction == 'R':
            head = (head[0], head[1] + 1)
        elif direction == 'D':
            head = (head[0] + 1, head[1])

        # Check if the snake has hit the wall or itself
        if (head in self.snake or head[0] < 0 or head[0] >= self.height or
            head[1] < 0 or head[1] >= self.width):
            return -1

        # Insert the new head position
        self.snake.insert(0, head)

        # Check if the snake eats food
        if self.food and head == tuple(self.food[0]):
            self.food.pop(0)
            self.snake.append(tail)  # Grow the snake
            self.score += 1

        return self.score

# Example usage
game = SnakeGame(3, 2, [[1, 1], [1, 0]])
print(game.move('R'))  # 0
print(game.move('D'))  # 1 (eats food)
print(game.move('D'))  # -1 (hits the wall)