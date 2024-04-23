from datetime import datetime

class Airline:
    def __init__(self, airline_id, name):
        self.id = airline_id
        self.name = name
        self.planes = []

class Airplane:
    def __init__(self, airplane_id, company):
        self.id = airplane_id
        self.current_location = None
        self.company = company
        self.next_flights = []

    def fly(self, destination):
        if self.available_on_date(datetime.now().date(), destination.city):
            flight = Flight(datetime.now().date(), self.current_location, destination, self)
            self.next_flights.append(flight)
            self.next_flights.sort(key=lambda x: x.date)

    def location_on_date(self, date):
        for flight in self.next_flights:
            if flight.date > date:
                return flight.origin
            elif flight.date == date:
                return flight.destination
        return self.current_location

    def available_on_date(self, date, location):
        if self.location_on_date(date) == location and len(self.next_flights) == 0:
            return True
        return False

class Flight:
    def __init__(self, date, origin, destination, plane):
        self.date = date
        self.origin = origin
        self.destination = destination
        self.plane = plane
        self.id = f"{destination.city}-{plane.company.id}-{date}"

    def take_off(self):
        self.plane.current_location = self.destination

    def land(self):
        self.plane.current_location = self.origin

class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, datetime):
        for plane in self.planes:
            if plane.available_on_date(datetime.date(), self.city):
                flight = Flight(datetime.date(), self, destination, plane)
                plane.next_flights.append(flight)
                plane.next_flights.sort(key=lambda x: x.date)
                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)
                return flight
        return None

    def info(self, start_date, end_date):
        print(f"Scheduled flights from {self.city} between {start_date} and {end_date}:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"Flight ID: {flight.id}, Date: {flight.date}, Destination: {flight.destination.city}")

# Test the system
if __name__ == "__main__":
    # Create Airlines
    airline1 = Airline("AA", "Airline A")
    airline2 = Airline("BB", "Airline B")

    # Create Airports
    airport1 = Airport("AAA")
    airport2 = Airport("BBB")

    # Create Airplanes
    plane1 = Airplane(1, airline1)
    plane2 = Airplane(2, airline2)

    # Add planes to airlines and airports
    airline1.planes.append(plane1)
    airline2.planes.append(plane2)
    airport1.planes.append(plane1)
    airport2.planes.append(plane2)

    # Schedule flights
    flight1 = airport1.schedule_flight(airport2, datetime.now())
    flight2 = airport2.schedule_flight(airport1, datetime.now())

    # Display scheduled flights
    airport1.info(datetime.now().date(), datetime.now().date())
    airport2.info(datetime.now().date(), datetime.now().date())
