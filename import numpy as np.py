import time
from geopy.distance import geodesic

class Station:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Customer:
    def __init__(self):
        self.vehicle_type = None
        self.has_batteries = False
        self.location = None
        self.battery_level = None

    def get_vehicle_type(self):
        while True:
            vehicle_type = input("Are you a bike owner or cargo owner? Enter 'bike' or 'cargo': ").lower()
            if vehicle_type in ['bike', 'cargo']:
                self.vehicle_type = vehicle_type
                break
            else:
                print("Invalid input. Please enter 'bike' or 'cargo'.")

    def get_location(self):
        if self.vehicle_type == 'bike':
            try:
                latitude = float(input("Enter your latitude: "))
                longitude = float(input("Enter your longitude: "))
                self.location = (latitude, longitude)
            except ValueError:
                print("Invalid input. Please enter numeric values for latitude and longitude.")

    def get_batteries_info(self):
        if self.vehicle_type == 'cargo':
            batteries_info = input("Do you have batteries? Enter 'yes' or 'no': ").lower()
            self.has_batteries = batteries_info == 'yes'
            if self.has_batteries:
                try:
                    self.battery_level = float(input("Enter your battery charge level (0-100): "))
                    if not (0 <= self.battery_level <= 100):
                        raise ValueError
                except ValueError:
                    print("Invalid input. Please enter a numeric value between 0 and 100.")

class StationChooser:
    def __init__(self):
        self.stations = [
            Station("Station A", (10.0, 20.0)),
            Station("Station B", (15.0, 25.0)),
            Station("Station C", (8.0, 18.0)),
            Station("Station D", (20.0, 30.0)),
            Station("Station E", (12.0, 22.0)),
        ]

    def suggest_destinations(self):
        print("EV CHARGING BIKE")

    def predict_destination(self, customer):
        if customer.vehicle_type == 'bike':
            nearest_station = min(self.stations, key=lambda station: geodesic(customer.location, station.location).miles)
            return nearest_station.name
        elif customer.vehicle_type == 'cargo' and customer.has_batteries:
            return "station"
        elif customer.vehicle_type == 'cargo' and not customer.has_batteries:
            return "solar farm"

def main():
    station_chooser = StationChooser()
    station_chooser.suggest_destinations()

    time.sleep(2)  # Delay for 2 seconds

    customer = Customer()
    customer.get_vehicle_type()

    if customer.vehicle_type == 'bike':
        customer.get_location()

    if customer.vehicle_type == 'cargo':
        customer.get_batteries_info()

    destination = station_chooser.predict_destination(customer)

    print("After considering the input,")
    time.sleep(1)  # Delay for 1 second

    if customer.vehicle_type == 'bike':
        nearest_station = min(station_chooser.stations, key=lambda station: geodesic(customer.location, station.location).miles)
        print(f"The user should go to {destination} (Distance: {geodesic(customer.location, nearest_station.location).miles:.2f} miles)")
        time.sleep(1.5)
        print(f"......Bike owner from location {customer.location} is going to {destination}")

        # After reaching the station, ask if the user is a bike owner or cargo owner
        time.sleep(1.5)
        print("The user reached the station")
        time.sleep(1)
        user_type_after_reaching = input("Are you a bike owner or cargo owner now? Enter 'bike' or 'cargo': ").lower()

        if user_type_after_reaching == 'bike':
            try:
                battery_level = float(input("Enter your battery charge level (0-100): "))
                if not (0 <= battery_level <= 100):
                    raise ValueError
                print(f"Your bike's battery level is: {battery_level}%")
            except ValueError:
                print("Invalid input. Please enter a numeric value between 0 and 100.")

    elif customer.vehicle_type == 'cargo':
        print(f"The user should go to {destination}")
        time.sleep(2)
        print(f"......Cargo owner is going to {destination}")

if __name__ == "__main__":
    main()
