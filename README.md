# Airport Plane Management System

This Python script simulates an airport managing plane arrivals and departures using a priority queue. It consists of classes representing planes, the airport, and functions to simulate plane arrivals and the airport's management of permissions.

## Requirements

- Python 3.x

## Usage

1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. Run the script:
   ```bash
   python Airport.py
   ```

## Code Structure

- **PriorityQueue**: A custom implementation of a priority queue used by the airport to manage planes.
- **Plane**: Represents a plane with a name and type. Contains methods to get and set plane attributes.
- **Airport**: Simulates an airport managing plane arrivals and departures. It uses a priority queue to prioritize landing, takeoff, and emergency landing requests.
- **simulate_planes()**: Function to simulate plane arrivals and enqueue them into the airport.
- **simulate_airport()**: Function to simulate the airport's management of plane permissions.
- **Main**: Entry point of the script. It initializes the airport, starts threads for simulating plane arrivals and airport management, and waits for threads to complete.

## Features

- Generates random plane names and types.
- Manages plane permissions based on priority (landing, takeoff, emergency landing).
- Simulates plane arrivals and enqueues them into the airport.
- Simulates the airport's management of plane permissions.

## Example Output

```
Plane XG1232 asks for takeoff
Plane JB4335 asks for emergency landing
Plane DC3357 asks for landing
CONTROL: DC3357 has permission to land
CONTROL: XG1232 has permission to takeoff
CONTROL: JB4335 has permission to emergency land
Plane YB5442 asks for takeoff
Plane XT1221 asks for landing
CONTROL: XT1221 has permission to land
CONTROL: YB5442 has permission to takeoff
Simulation Complete
```
