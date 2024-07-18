# Simple exmaple of a class of creating a representing an X and  Y value
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
p = Point(2, 8)
print(p.x)
print(p.y)

# A program of an airline where an airline has to keep track of 
# booking passengers in a flight and making sure no flight gets over-booked
# and keeps track of pasengers in that flight.

# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []
    
#     def add_passengers(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True
#         # if self.open_seats() == 0:
        
#     def open_seats(self):
#         return self.capacity - len(self.passengers)
 
# flight = Flight(3)
# people = ['Harry', 'Ron', 'Hermione','Ginny']
# for person in people:
#     success = flight.add_passengers(person)
#     if success:
#         print(f'Added {person} to flight successfully')
#     else:
#         print(f'No available seats for {person}')
        
        
        
# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passenger = []
        
#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passenger.append(name)
#         return True
        
        
#     def open_seats(self):
#         return self.capacity - len(self.passenger)

# flight = Flight(3)
# names = ['Harry', 'Hermione', 'Ron', 'Wise', 'Grace']

# for name in names:
#         success = flight.add_passenger(name)
#         if success:
#             print(f'Added {name} to flight successfully')
#         else:
#             print(F'No available seats for {name}')
    
            
            
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
    def add_passenger(self, name):
        if not self.open_seat():
            return False
        self.passenger.append(name)
        return False
    
    def open_seats(self):
        return self.capacity - len(self.passenger)
        

flight = Flight(5)
names = ['wise', 'john', 'peter', 'james', 'catherine']
for name in names:
    success = flight.add_passenger(name)
    if success:
        print(f'Added {name} successfully to flight')
    else:
        print(f'No available seats for {name}')       