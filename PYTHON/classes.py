class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []
    def add_passenges(self, name):
        if not self.open_seats(): #equal to if open_seats() == 0
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Larry", "Merry", "Garry", "Terry"]
for person in people:
    avaliable = flight.add_passenges(person)
    if avaliable:
        print(f"Added {person} successfully")
    else:
        print(f"There's no avaliable seats for {person}")