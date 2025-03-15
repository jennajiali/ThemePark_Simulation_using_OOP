from Themepark_classes import Ride, ThemePark
import numpy as np

def test_theme_park():
    rides = [
        Ride(ride_id=1, ride_name="Ride One", ride_rate=1.1),
        Ride(ride_id=2, ride_name="Ride Two", ride_rate=0.7),
        Ride(ride_id=3, ride_name="Ride Three", ride_rate=0.8)
        ]

    transition_matrix = np.array([
        [0, 0.3, 0.4, 0.3, 0.0],  # From Arrival
        [0, 0.5, 0.3, 0.1, 0.1],  # From Ride One
        [0, 0.4, 0.1, 0.3, 0.2],  # From Ride Two
        [0, 0.3, 0.3, 0.2, 0.2],  # From Ride Three
        [0, 0.0, 0.0, 0.0, 1.0]   # From Exit: just to make it square
    ])
    arrival_rate = 0.5
    park = ThemePark(rides, arrival_rate, transition_matrix)
    park.simulate(max_time=10, verbose=True)
    
    # Check attributes
    print("")
    print(f"Total customers: {len(park.customers)}")

    # Assert that the number of customers is non-negative
    assert len(park.customers) >= 0
    
    for customer in park.customers:
        print(f"Customer {customer.customer_id} - Arrival Time: {customer.arrival_time}, "
              f"Rides Taken: {len(customer.path)}, Total Wait Time: {sum(customer.wait_times)}, "
              f"Total Ride Time: {sum(customer.ride_times)}")
    # Check final ride queues
    print("")
    for ride in park.rides:
        print(ride)

test_theme_park()  # Should produce a different output each time


