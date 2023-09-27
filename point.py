class Point:
    @staticmethod
    def get_position(position: str) -> (int, int):
        assert len(position) == 2
        y = 8 - int(position[1])
        x = ord(position[0]) - 97
        return y, x

    @staticmethod
    def get_position_int(y: int, x: int) -> str:
        print(str(chr(97 + x) + str(8 - y)))
        return str(chr(97 + x) + str(8 - y))
