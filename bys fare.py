class Vehicle:
    def __init__(self, capacity, fare_per_person):
        self.capacity = capacity
        self.fare_per_person = fare_per_person

    def calculate_fare(self):
        return self.capacity * self.fare_per_person


class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare




if __name__ == "__main__":
    capacity = int(input("Enter number of passengers: "))
    fare_per_person = float(input("Enter fare per person: "))

    bus = Bus(capacity, fare_per_person)
    total_fare = bus.calculate_fare()

    print(f"\nTotal Bus Fare (including 10% maintenance): ₹{total_fare:.2f}")