class Point:
    def __init__(self, position: str):
        # TODO use some try except assert
        assert len(position) == 2
        self.y, self.x = self.get_position(position)

    def get_position(self, position: str) -> (int, int):
        return int(position[1]) - 1, ord(position[0]) - 97
