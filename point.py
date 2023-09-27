class Point:
    @staticmethod
    def get_position(position: str) -> (int, int):
        assert len(position) == 2
        y = 8 - int(position[1])
        x = ord(position[0]) - 97
        return y, x
