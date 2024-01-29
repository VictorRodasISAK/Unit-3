class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

    def get_size_engine(self, capacity):
        if self.fuel_type.lower() == "electric":
            print(f"Engine Capacity {capacity} kW/h")
        else:
            print(f"Engine Capacity {capacity} Liters")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine

    def start(self):
        if self.engine:
            print(f"{self.brand} {self.model}'s engine is starting.")
            self.engine.start()
        else:
            print("No engine set for the vehicle.")

    def stop(self):
        if self.engine:
            print(f"{self.brand} {self.model}'s engine is stopping.")
            self.engine.stop()
        else:
            print("No engine set for the vehicle.")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors, license_plate):
        super().__init__(brand, model)
        self.num_doors = num_doors
        self.num_passengers = None
        self.license_plate = license_plate

    def set_number_passengers(self, num_passengers):
        self.num_passengers = num_passengers
        print(f"Number of passengers set to: {self.num_passengers}")

    def space_available(self, requested_passengers):

        while self.num_passengers is None or self.num_passengers < requested_passengers:
            requested_passengers = int(input("Too many passengers, enter a new amount of passengers: "))

        delete = input("Do you want to delete passengers?: Y - Yes, N - No ").lower()

        if delete == "y":
            number = int(input("Enter how many passengers you want to delete: "))
            self.num_passengers -= number

        print(f"Available space for {self.num_passengers} passengers more.")


class LicensePlate:
    def __init__(self, letter, serial_number):
        self.letter = letter
        self.serial_number = serial_number

    def get_license_plate(self):
        return f"{self.letter}{str(self.serial_number)}"


# Example
electric_engine = Engine("Electric")
license_plate = LicensePlate("あ", "123-512")
electric_vehicle = Car("Mitsubishi", "2016", 4, license_plate)
print("License Plate:", electric_vehicle.license_plate.get_license_plate())
electric_engine.get_size_engine(80)
electric_vehicle.set_number_passengers(6)
electric_vehicle.space_available(int(input("Enter how many passengers: ")))
electric_vehicle.set_engine(electric_engine)
electric_vehicle.start()
electric_vehicle.stop()



