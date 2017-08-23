class RaceCar():
    def __init__(self, color, laps=10, fuel_remaining=None, **kwargs):
        self.fuel_remaining = fuel_remaining
        self.color = color
        self.laps = laps

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining = self.fuel_remaining - length * 0.125
        self.laps += 1

RaceCar(blue, 10, 10)