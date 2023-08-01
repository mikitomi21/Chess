class Point:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def get_position(self) -> (int, int):
        return self.y, self.x
