class Point:
    def __init__(self, position: str):
        # TODO use some try except assert
        assert len(position) == 2
        self.y, self.x = self.get_position(position)

    @staticmethod
    def get_position(position: str) -> (int, int):
        return int(position[1]) - 1, ord(position[0]) - 97
