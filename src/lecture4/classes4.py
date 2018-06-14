class Flight:
    
    counter = 1
    
    def __init__(self, origin, destination, duration):
        
        # flight id
        self.id = Flight.counter
        Flight.counter+=1
        
        # flight passengers
        self.passengers = []
        
        # flight information
        self.origin = origin
        self.destination = destination
        self.duration = duration
        
    def print_info(self):
        print(f"id: {self.id}")
        print(f"origin: {self.origin}")
        print(f"destination: {self.destination}")
        print(f"duration: {self.duration}")
        print("passengers:", self.passengers)
        print()
    
    def delay(self, amount):
        self.duration += amount 
        
    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id
        
class Passenger():
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name
        
    def __str__(self):
        return self.name + ""
        
def main():
    f1 = Flight("New York", "Paris", 500)
    f2 = Flight("Toronto", "Paris", 400)
    
    alice = Passenger("alice")
    bob = Passenger("bob")
    
    f1.add_passenger(alice)
    f1.add_passenger(bob)
    
    f1.print_info()
    f2.print_info()
    
if __name__ == '__main__':
    main()