import random
from collections import deque
import numpy as np

class PriorityQueue:
    """
    Represents a priority queue in the theme park simulation that arranges events 
    in ascending order of their priority value (event time). 
    
    Attribute:
    queue (list): a list of tuples representing events. Each tuple contains:
            - event_time (float): The time at which the event occurs.
            - ride_id (int): The unique identifier of the ride or 0 for a new customer arrival.
    """
    def __init__(self):
        """Initialises an empty priority queue."""
        self._queue = []

    @property
    def queue(self):
        """Returns the current state of the priority queue."""
        return self._queue

    def push(self, event_time, ride_id):
        """
        Inserts a new event into the priority queue and sorts it by event_time.

        Parameters:
        - event_time (int or float): The time at which the event occurs.
        - ride_id (int): The ID of the associated ride.
        
        Raises ValueError if event_time is not a non-negative number or ride_id is not a non-negative integer.
        """
        if not isinstance(event_time, (int, float)) or event_time < 0:
            raise ValueError("event_time must be a non-negative number.")
        if not isinstance(ride_id, int) or ride_id < 0:  
            raise ValueError("ride_id must be a non-negative integer.")
        
        self._queue.append((float(event_time), ride_id))
        # Sort the queue by event_time
        get_first_element = lambda event: event[0]
        self._queue.sort(key = get_first_element)

    def popleft(self):
        """
        Removes and return the first item in queue.

        Returns:
        - tuple (event_time, ride_id): the event with the smallest event_time.

        Raises IndexError if the queue is empty.
        """
        if not self._queue:
            raise IndexError("Cannot popleft because the priority queue is empty.")
        return self._queue.pop(0)
    


class Customer:
    """
    Represents a customer visiting the theme park.
    
    Attributes: 
    - customer_id (int): The unique identifier of the customer.
    - arrival_time (float): The time the customer arrives at the park.
    - path (list[int]): The sequence of ride_id (int) the customer visits.    
    - ride_times (list[float]): Time spent on each ride.
    - wait_times (list[float]): Time spent in each ride's queue.
    """

    def __init__(self, customer_id, arrival_time):
        """
        Initialises a Customer object with their ID and arrival time.

        Parameters:
        - customer_id (int): The unique ID of the customer.
        - arrival_time (int or float): The time at which the customer arrives at the park.
        
        Raises ValueError if
        - customer_id is not an integer or 
        - arrival_time is not a non-negative number
        """
        
        if not isinstance(customer_id, int):
            raise ValueError("customer_id must be an integer.")
        if not isinstance(arrival_time, (int, float)) or arrival_time < 0:
            raise ValueError("arrival_time must be a non-negative number.")
    
        # Private attributes to prevent accidental modification of the customer record by external code
        self._customer_id = customer_id
        self._arrival_time = float(arrival_time)
        self._path = []
        self._ride_times = []
        self._wait_times = []

    # Use getters to access the read-only private attributes
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def arrival_time(self):
        return self._arrival_time
    
    @property
    def path(self):
        return self._path

    @property
    def ride_times(self):
        return self._ride_times

    @property
    def wait_times(self):
        return self._wait_times

    def record_ride(self, ride_id, ride_time, wait_time):
        """
        Records the details related to the ride the customer has done.

        Parameters:
        - ride_id (int): The ID of the ride. 
        - ride_time (int or float): Time spent on the ride.
        - wait_time (int or float): Time spent waiting in the queue.
        
        Raises ValueError if
        - ride_id is not a non-negative integer or 
        - ride_time or wait_time is not a non-negative number
        """
        
        if not isinstance(ride_id, int) or ride_id < 0:
            raise ValueError("ride_id must be a non-negative integer.")
        if not isinstance(ride_time, (int, float)) or ride_time < 0:
            raise ValueError("ride_time must be a non-negative number.")
        if not isinstance(wait_time, (int, float)) or wait_time < 0:
            raise ValueError("wait_time must be a non-negative number.")
        self._path.append(ride_id)
        self._ride_times.append(float(ride_time))
        self._wait_times.append(float(wait_time))



class Ride(deque):
    """
    Represents a theme park ride with a customer queue.
    Inherits from deque to process the queue of customers on a First In, First Out basis.
    
    Attributes:
    - ride_id (int): a unique positive identifier of the ride, or 0 for a new customer arrival.
    - ride_name (str): The name of the ride.
    - ride_rate (float): The rate at which the ride processes customers. 
    - customers_processed (int): A count of the number of customers the ride has processed.
    - total_ride_time (float): The cumulative time spent on the ride by customers.
    - queue_entry_times (dict): A ditionary mapping customer IDs to their queue entry times. 
    """
    def __init__(self, ride_id, ride_name, ride_rate):
        """
        Initialises a Ride object with its ID, name, and customer-processing rate.
        
        Parameters:
        - ride_id (int): a unique positive identifier of the ride, or 0 for a new customer arrival.
        - ride_name (str): The name of the ride.
        - ride_rate (float): Rate at which the ride processes customers (positive number).
        
        Raises ValueError if
        ride_id is not a positive integer, or ride_name is not of type string, or ride_rate is not a positive number.
        """

        super().__init__()  # Initialise the super class deque
        
        if not isinstance(ride_id, int) or ride_id < 0:
            raise ValueError("ride_id for a Ride instance must be a non-negative integer.")
        if not isinstance(ride_name, str):
            raise ValueError("ride_name should be a string.")
        if not isinstance(ride_rate, (int, float)) or ride_rate <= 0:
            raise ValueError("ride_rate must be a positive number.")
        self._ride_id = ride_id
        self._ride_name = ride_name
        self._ride_rate = ride_rate
        self._customers_processed = 0
        self._total_ride_time = 0
        self._queue_entry_times = {}  # Dictionary to store queue entry times of customers

    @property
    def ride_id(self):
        return self._ride_id

    @property
    def ride_name(self):
        return self._ride_name

    @property
    def ride_rate(self):
        return self._ride_rate

    @property
    def customers_processed(self):
        return self._customers_processed

    @property
    def total_ride_time(self):
        return self._total_ride_time
    
    def append(self, customer_tuple):
        """
        Represents the arrival of a customer at the ride queue.
        
        Parameters:
        customer_tuple (tuple): contains a Customer object and their queue entry time.
        """
        super().append(customer_tuple)  # Add the customer to the queue
        customer, queue_entry_time = customer_tuple
        self._queue_entry_times[customer.customer_id] = queue_entry_time  # Store queue entry time
    
    def carry_customer(self, current_time):
        """
        Removes the first customer in the queue and processes them on the ride.

        Parameter:
        current_time (int or float): a number representing the current time in the simulation.

        Returns:
        tuple of the form (customer, completion_time)
                - customer: The Customer object processed.
                - completion_time: The time the customer finishes the ride.
        
        Raises 
        - IndexError if the ride queue is empty i.e. no customers.
        - ValueError if current_time is not a number. 
        """
        if not isinstance(current_time, (int, float)):
            raise ValueError("current_time must be a number.")
        if not self:
            raise ValueError("The ride queue is empty so there is no customer to carry.")

        # Process the first customer in the queue
        customer, queue_entry_time = self.popleft()  
        self._customers_processed += 1

        # Generate ride time with the exponential rate parameter
        ride_time = random.expovariate(self._ride_rate)
        completion_time = current_time + ride_time
        self._total_ride_time += ride_time

        return (customer, completion_time)
    
    def get_queue_entry_time(self, customer_id):
        """
        Retrieves the queue entry time for a given customer ID.

        Parameter:
        customer_id (int): The ID of the customer.

        Returns:
        float: The queue entry time of the customer if they are in the queue, else None.
        """
        return self._queue_entry_times.get(customer_id, None)

    def __str__(self):
        """
        Return a formatted string outlining all customers in the queue by their customer_ids.

        Returns:
        - str: A string showing the list of customer IDs in the queue for this ride.
        """
        customer_ids = [customer.customer_id for customer, arrival_time in self]
        return f"Queue for the ride {self.ride_id}, {self.ride_name}: {customer_ids}"
    


class ThemePark:
    """
    Represents the theme park simulation.

    Attributes:
    - rides (list): an ordered collection of Ride instances in increasing order of ride_id.
    - arrival_rate (float): The rate at which customers arrive at the park. Must be positive.
        Assumes customers arrive according to a Poisson process with rate arrival_rate.
        The time until the next customer arrival is exponentially distributed with mean 1/arrival_rate.
    - transition_matrix (numpy.ndarray): Square matrix representing ride transition probabilities.
    - event_queue (PriorityQueue): Queue managing simulation events.
    - customers (list): List of all customers in the simulation.
    """

    def __init__(self, rides, arrival_rate, transition_matrix):
        """
        Initialises the theme park with rides, arrival rate, and a transition matrix.

        Parameters:
        - rides (list of Ride): an ordered collection of Ride instances in increasing order of ride_id.
        - arrival_rate (int or float): The rate at which customers arrive at the park. Must be positive.
        - transition_matrix (numpy.ndarray): Square matrix representing ride transition probabilities.

        Raises ValueError if arrival_rate is not positive or transition_matrix is not a square numpy array.
        """
        self._rides = rides
        if not isinstance(arrival_rate, (int, float)) or arrival_rate <= 0:
            raise ValueError("arrival_rate must be a positive number.")
        self._arrival_rate = float(arrival_rate)
        if not isinstance(transition_matrix, np.ndarray) or transition_matrix.shape[0] != transition_matrix.shape[1]:
            raise ValueError("transition_matrix must be a square numpy array.")
        self._transition_matrix = transition_matrix
        self._event_queue = PriorityQueue()
        self._customers = []

    @property
    def rides(self):
        return self._rides

    @property
    def arrival_rate(self):
        return self._arrival_rate

    @property
    def transition_matrix(self):
        return self._transition_matrix

    @property
    def event_queue(self):
        return self._event_queue

    @property
    def customers(self):
        return self._customers

    def route_customer(self, ride_id):
        """
        Generates the next ride's ID probabilistically based on the transition matrix. 
        With replacement, randomly selects the next ride based on the probabilities given the current ride_id.
        
        Parameters:
        ride_id (int): The ID of the current ride (1-based index), or 0 for a customer entrance.

        Returns:
        int: The ID of the next ride, or the exit indicator.
        """
        row = self._transition_matrix[ride_id] # List of transition probabilities given the current ride
        dim = len(row)   # Length of the ride indices
        next_ride_id = np.random.choice(a=range(dim), replace=True, p=row)
        return int(next_ride_id)

    def simulate(self, max_time, verbose=False):
        """
        Performs a simulation of the theme park events for a given duration (max_time).

        Parameters:
        - max_time (float): The maximum simulation time. The simulation stops when current_time exceeds max_time.
        - verbose (bool): If True, prints a log whenever a customer entered or is processed by a ride. False by default (no logs).
        """
        num_rides = len(self._rides)
        current_time = 0  # Initialise the simulation time
        
        # Generate the first customer arrival and schedule this event in the priority queue
        customer_id = 1
        t = random.expovariate(self._arrival_rate)  
        self._event_queue.push(event_time=t, ride_id=0)

        # Continue processing the events until time exceeds the maximum or the event queue is empty
        while self._event_queue.queue and current_time < max_time: 
            current_time, ride_id = self._event_queue.popleft()  # Get the next event

            if int(ride_id) == 0:  # Event being a new customer arrival
                # Process their arrival
                arrival_time = current_time
                c = Customer(customer_id, arrival_time)
                self._customers.append(c) 

                # Route them to the next event (ride or exit)
                next_ride_id = self.route_customer(ride_id)
                if next_ride_id <= num_rides:  # If they are not exiting
                    for ride in self._rides:
                        if ride.ride_id == next_ride_id:
                            ride.append((c, arrival_time))
                    # Schedule an event for this ride
                    self._event_queue.push(arrival_time, next_ride_id)
                
                if verbose:
                    print(f"Customer {c.customer_id} arrived at time {arrival_time}.")

                # Schedule the next customer arrival event (then sorted by the priority queue)
                customer_id += 1 
                next_arrival_time = current_time + random.expovariate(self._arrival_rate)
                self._event_queue.push(next_arrival_time, ride_id=0)

            else:  # Event being a customer completing a ride
                for ride in self._rides:
                    if ride.ride_id == int(ride_id):
                        c, completion_time = ride.carry_customer(current_time)
                        queue_entry_time = ride.get_queue_entry_time(c.customer_id)
                        if current_time < queue_entry_time:  # Customer arrived and immediately boarded the ride
                            wait_time = 0
                        else: # Customer waited in the queue
                            wait_time = current_time - queue_entry_time
                        c.record_ride(ride_id, completion_time - current_time, wait_time)

                        # Route the customer to a next ride or exit
                        next_ride_id = self.route_customer(ride_id)
                        if next_ride_id <= num_rides: 
                            for next_ride in self._rides:
                                if next_ride.ride_id == next_ride_id:
                                    # Check if the ride can be completed within the remaining time
                                    expected_ride_time = random.expovariate(next_ride.ride_rate)
                                    if completion_time + expected_ride_time <= max_time:
                                        next_ride.append((c, completion_time))
                                        self._event_queue.push(completion_time, next_ride_id)
                                    else:
                                        if verbose:
                                            print(f"Customer {c.customer_id} cannot start {next_ride.ride_name} due to insufficient remaining time.")
                            
                        if verbose:
                            print(f"Customer {c.customer_id} completed {ride.ride_name} at time {completion_time}.")

    def __str__(self):
        """
        Return the current status of the ride queues in the park.

        Returns:
        str: A string representing the status of all rides.
        """
        lst = [str(ride) for ride in self._rides]
        status = "\n".join(lst) # Concatenate the ride strings with a new line separator
        return status
    

