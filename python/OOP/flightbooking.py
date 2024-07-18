class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passanger = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passanger.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passanger)
        
flight = Flight(3)
names = ['Wise', 'Peter', 'John', 'James']
for person in names:
    success = flight.add_passenger(person)
    if success:
        print(f'Added {person} succefully to the flight')
    else:
        print(f'Not added {person} to flight')