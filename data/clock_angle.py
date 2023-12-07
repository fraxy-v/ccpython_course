class Minute:
    def __init__(self, minute: int):
        self._minute = minute


    def is_valid(self) -> bool:
        return self._minute >= 0 and self._minute < 60


    def to_angle(self) -> int:
        return self._minute * 6


class Hour:
    def __init__(self, hour: int):
        self._hour = hour


    def is_valid(self) -> bool:
        return self._hour >= 0 and self._hour <= 24

    def to_angle(self, minute : Minute) -> int:
        h = self._hour % 12
        return round(h * 30 + minute._minute * 0.5)


def clock_angle(hour: Hour, minute: Minute) -> int:
    # Add implementation here
    return None
