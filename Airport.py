from PriorityQueue import PriorityQueue, PriorityQueueNode
import random
import string
from time import sleep 
import threading

random.seed(2)


def generate_plane_name():
    """Generates a random plane name."""
    letters = string.ascii_uppercase
    digits = ''.join(random.choices(string.digits, k=4))
    name = ''.join(random.choices(letters, k=2)) + digits
    return name

def generate_plane():
    """Generates a random plane with a random type."""
    random_type = random.choice(['landing', 'takeoff', 'emergency landing'])
    plane = Plane(random_type)
    return plane

class Plane():
    """Represents a plane with a name and type."""
    def __init__(self, type: str) -> None:
        """Initialize the plane with a type and generate a random name."""
        self.name = generate_plane_name()
        self.type = type

    def get_name(self):
        """Returns the name of the plane."""
        return self.name
    
    def __str__(self):
        """Returns a string representation of the plane."""
        return f'Plane {str(self.name)} asks for {str(self.type)}'
    
    def get_type(self):
        """Returns the type of the plane."""
        return self.type

    def set_type(self, value):
        """Sets the type of the plane."""
        self.type = value

class Airport():
    """Simulates an airport managing plane arrivals and departures."""
    def __init__(self) -> None:
        """Initializes the airport with a priority queue, locks, and event."""
        self.pq = PriorityQueue() # Priority queue for managing planes
        self.arrival_counter = 0
        self.lock = threading.Lock()
        self.simulation_completed = threading.Event()  # Event to signal simulation completion
        self.total_iterations = 4  # Total number of iterations
        self.iteration_count = 0  # Counter for tracking iterations

    def enqueue(self, plane: Plane):
        """Enqueues a plane into the priority queue based on its type."""
        with self.lock:
            if plane.get_type() == 'landing':
                self.pq.insert(plane.get_name(), 1)
            elif plane.get_type() == 'takeoff':
                self.pq.insert(plane.get_name(), 0)
            elif plane.get_type() == 'emergency landing':
                self.pq.insert(plane.get_name(), 2)
            else:
                print("Plane cannot be enqueued")

    def grant_permission(self):
        """Grants permission for a plane to land, takeoff, or make an emergency landing."""
        with self.lock:
            if not self.pq.is_empty():
                id, plane_name, priority = self.pq.remove()
                
                if priority == 1: 
                    print("\033[93mCONTROL:\033[0m", f'{plane_name} has permission to land')
                    self.iteration_count += 1
                elif priority == 0:
                    print("\033[93mCONTROL:\033[0m", f'{plane_name} has permission to takeoff')
                    self.iteration_count += 1
                elif priority == 2:
                    print("\033[93mCONTROL:\033[0m", f'{plane_name} has permission to emergency land')
                    self.iteration_count += 1
                else:
                    print("Permission not granted")

                if self.iteration_count >= self.total_iterations:
                    self.simulation_completed.set()

def simulate_planes(airport: Airport):
    """Simulates plane arrivals and enqueues them into the airport."""
    while not airport.simulation_completed.is_set():
        sleep(random.uniform(0.5, 0.6))
        plane = generate_plane()
        print(plane)
        airport.enqueue(plane)

def simulate_airport(airport: Airport) -> None:
    """Simulates the airport managing plane permissions."""
    while not airport.simulation_completed.is_set():
        sleep(1.2)
        airport.grant_permission()  

if __name__ == "__main__":
    
    airport = Airport()

    plane_requests_thread = threading.Thread(target=simulate_planes, args=(airport,))
    airport_simulation_thread = threading.Thread(target=simulate_airport, args=(airport,))
    plane_requests_thread.start()
    airport_simulation_thread.start()

    plane_requests_thread.join()
    airport_simulation_thread.join()

    print("Simulation Complete")
