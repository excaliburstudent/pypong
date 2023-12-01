class Paddle:

    WIDTH = 10
    HEIGHT = 75
    
    def __init__(self, court, which):
        self.x = court.get_paddle_x(which) - Paddle.WIDTH // 2
        self.y = court.get_paddle_y() - Paddle.HEIGHT // 2
        