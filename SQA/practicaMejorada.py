# Definición de la clase Flight
# Sistema de reservas de vuelo python 
# 1Reservar asientos para pasajeros, con verificación de disponibilidad.
# 2Cancelar reservas de asientos para pasajeros específicos.
# 3Listar todos los pasajeros actuales en el vuelo.
class Flight:
    # Método inicializador que establece los atributos del vuelo
    def __init__(self, flight_number, origin, destination, seats):
        self.flight_number = flight_number  # Número de vuelo
        self.origin = origin  # Origen del vuelo
        self.destination = destination  # Destino del vuelo
        self.seats = seats  # Número de asientos disponibles
        self.passengers = []  # Lista de pasajeros en el vuelo

    # Método para reservar un asiento para un pasajero
    def book_seat(self, passenger):
        # Si hay asientos disponibles
        if len(self.passengers) < self.seats:
            self.passengers.append(passenger)  # Añadir el pasajero a la lista
            print(f"Seat booked for {passenger.name} on flight {self.flight_number}")
        else:
            print("No available seats.")  # Mensaje si no hay asientos disponibles

    # Método para cancelar la reserva de un asiento para un pasajero
    def cancel_seat(self, passenger):
        # Intentar remover al pasajero de la lista
        try:
            self.passengers.remove(passenger)  # Remover el pasajero de la lista
            print(f"Seat canceled for {passenger.name} on flight {self.flight_number}")
        except ValueError:
            print(f"{passenger.name} does not have a seat on this flight.")  # Mensaje si el pasajero no está en la lista

    # Método para listar todos los pasajeros en el vuelo
    def list_passengers(self):
        for passenger in self.passengers:  # Recorrer la lista de pasajeros
            print(f"Passenger: {passenger.name}")  # Imprimir el nombre de cada pasajero

# Definición de la clase Passenger
class Passenger:
    # Método inicializador que establece el nombre del pasajero
    def __init__(self, name):
        self.name = name  # Nombre del pasajero

# Uso de ejemplo
flight = Flight("AB123", "New York", "Los Angeles", 2)  # Crear una instancia de Flight
passenger1 = Passenger("John Doe")  # Crear una instancia de Passenger
passenger2 = Passenger("Jane Smith")  # Crear una instancia de Passenger
passenger3 = Passenger("Jim Brown")  # Crear una instancia de Passenger

# Reservar asientos para los pasajeros
flight.book_seat(passenger1)
flight.book_seat(passenger2)
flight.book_seat(passenger3)  # Esto fallará ya que los asientos están limitados a 2

# Listar todos los pasajeros en el vuelo
flight.list_passengers()
# Cancelar la reserva del primer pasajero
flight.cancel_seat(passenger1)
# Listar todos los pasajeros en el vuelo nuevamente
flight.list_passengers()
