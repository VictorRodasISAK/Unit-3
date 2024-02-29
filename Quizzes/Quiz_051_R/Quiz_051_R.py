from Quizzes.Quiz_051.Quiz_051 import Airline

class Aircraft:
    def __init__(self, model: str, capacity: int):
        self.model = model
        self.capacity = capacity

    def get_info(self):
        return f"{self.model} (Capacity: {self.capacity})"

class Flight(Airline):
    def __init__(self, flight_number: str, origin: str, destination: str, departure_time: str, duration: list[int], aircraft: Aircraft):
        super().__init__(flight_number, origin, destination, departure_time, duration)
        self.aircraft = aircraft

    def get_flight_info(self):
        return f"{super().get_flight_info()} with {self.aircraft.get_info()}"

aircraft = Aircraft("Boeing 777", 550)
flight = Flight("AA123", "JFK", "LAX", "12:00", [5, 30, 0], aircraft)
print(flight.get_flight_info())