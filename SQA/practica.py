"""
class Flight:
    def __init__(self, flight_number, origin, destination, seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.passengers = []

    def book_seat(self, passenger):
        if len(self.passengers) < self.seats:
            self.passengers.append(passenger)
            print(f"Seat booked for {passenger.name} on flight {self.flight_number}")
        else:
            print("No available seats.")

    def cancel_seat(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"Seat canceled for {passenger.name} on flight {self.flight_number}")
        else:
            print(f"{passenger.name} does not have a seat on this flight.")

    def list_passengers(self):
        for passenger in self.passengers:
            print(f"Passenger: {passenger.name}")

class Passenger:
    def __init__(self, name):
        self.name = name

# Example usage
flight = Flight("AB123", "New York", "Los Angeles", 2)
passenger1 = Passenger("John Doe")
passenger2 = Passenger("Jane Smith")
passenger3 = Passenger("Jim Brown")

flight.book_seat(passenger1)
flight.book_seat(passenger2)
flight.book_seat(passenger3)  # This should fail as seats are limited to 2

flight.list_passengers()
flight.cancel_seat(passenger1)
flight.list_passengers()
"""
# A continuacion los cambios 
