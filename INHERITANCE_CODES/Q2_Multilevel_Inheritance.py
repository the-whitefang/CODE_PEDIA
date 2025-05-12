# Implement a multi-level inheritance hierarchy:
# 1. Class Vehicle → has max_speed attribute.
# 2. Class Car (inherits Vehicle) → has fuel_type attribute.
# 3. Class ElectricCar (inherits Car) → has battery_capacity attribute.

class Vehicle:
    def __init__(self,max_speed):
        self.max_speed = max_speed

    def show_speed(self):
        print(f"Max Speed = {self.max_speed}")

class Car(Vehicle):
    def __init__(self, max_speed, fuel_type):
        super().__init__(max_speed)
        self.fuel_type = fuel_type

    def show_fuel(self):
        print(f"Fuel Type = {self.fuel_type}")

class ElectricCar(Car):
    def __init__(self, max_speed, fuel_type, battery_capacity):
        super().__init__(max_speed, fuel_type)
        self.battery_capacity = battery_capacity

    def display_details(self):
        print(f"Max speed = {self.max_speed}")
        print(f"Fuel Type = {self.fuel_type}")
        print(f"Battery capacity = {self.battery_capacity}")




tesla = ElectricCar(250, "Electric", "100 kWh")
tesla.display_details()