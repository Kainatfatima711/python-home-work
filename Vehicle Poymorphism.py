from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    
class BMW(Vehicle):
    def start_engine(self):
        print("BMW engine started with keyless ignition.")

    def drive(self):
        print("Driving BMW smoothly with adaptive suspension.")

    def stop_engine(self):
        print("BMW engine stopped with auto shutdown.")


class Ferrari(Vehicle):
    def start_engine(self):
        print("Ferrari roars to life with a loud ignition sound.")


    def drive(self):
        print("Driving Ferrari with high speed and sharp handling.")

    def stop_engine(self):
        print("Ferrari engine shut down manually.")


def test_vehicle(vehicle: Vehicle):
    vehicle.start_engine()
    vehicle.drive()
    vehicle.stop_engine()
    print("-" * 40)



bmw_car = BMW()
ferrari_car = Ferrari()


test_vehicle(bmw_car)
test_vehicle(ferrari_car)