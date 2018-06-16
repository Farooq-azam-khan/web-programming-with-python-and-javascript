class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        
    def print_info(self):
        print(f"origin: {self.origin}")
        print(f"destination: {self.destination}")
        print(f"duration: {self.duration}")
        
        
def main():
    f1 = Flight("New York", "Paris", 500)
    f2 = Flight("Toronto", "Paris", 400)
    f1.print_info()
    f2.print_info()
    
if __name__ == '__main__':
    main()