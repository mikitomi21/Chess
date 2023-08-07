class Point:
    @staticmethod
    def get_position(position: str) -> (int, int):
        assert len(position) == 2
        return 8 - int(position[1]), ord(position[0]) - 97
