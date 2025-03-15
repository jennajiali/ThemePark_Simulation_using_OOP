# ThemePark_Simulation_using_OOP
STAT0040 coursework project for Objected-Oriented Programming


### Insights from the theme park simulation output:
relating to the file summary_output.csv generated using example_output_aggregation.py
- By aggregating the output data from Monday to Sunday across 4 weeks, the simulation illustrates that the number of customers visiting is much higher on weekends than weekdays, and it peaks on Sundays, reflecting that more people tend to visit the theme park for leisure during their days off.
- However, the average rides taken per customer appears lower during the peak times e.g. Sundays, and higher on the days when fewer customers are visiting e.g. Tuesdays.
- Customers also tend to spend more time waiting during peak times (from Fridays to Sundays) even though the average time they spent enjoying the rides are shorter (e.g. 0.84 the lowest on Sundays), likely due to longer queues or operational inefficiencies that arrised due to park congestion.


### A report on my solutions Themepark_classes.py

**Object-Oriented Programming**

- Encapsulation: each class bundled the relevant attribute data with methods that operate on the data. Getters with property decorators control read-only access to private attributes while preventing unintended modification of the customer records from outside the class. 

- Inheritance of Ride from deque reused the existing code, including append() and popleft(); it only adds specialised attributes/methods, keeping a clean interface. 

- Polymorphism: Ride customized append() method, overriding the function so it does different things depending on the data type being deque or Ride.

- Leveraging existing packages makes the class designs less redundant. 

**Data structure for certain attributes:**

1.	List as a mutable container in PriorityQueue.queue for storing a sequence of immutable tuples representing events and ordering them based on the first element. 

2.	Customer.path, .ride_times, .wait_times, and ThemePark.customers as lists to allow for e.g. duplicates in ride_ids and for easy mutability and order maintenance.

3.	Dictionary as a mutable structure with unique keys to map each customer_id to their queue_entry_times. Queue_entry_time is retrieved fast with customer_id as the key when processing a customer’s ride, and updated easily when that customer then queue for the next ride, ensuring one customer is queueing for only one queue at a time. 

**Possible Extensions to Make the Simulation More Realistic:**

1.	Height Restrictions:
    - Customer: Add a height attribute.
    - Ride: Add a min_height attribute.
    - ThemePark.simulate() checks to ensure customer height > ride min_height before adding them to the queue.


2.	Maximum Queue Lengths:
    - Ride: Add a max_queue_length attribute.
    - Add a method in ThemePark to track and retrieve queue lengths corresponding to each ride_id, using a dictionary. 
    - ThemePark.simulate() checks the queue length before adding a customer. If the queue is full, route the customer to a different ride.


The current four classes' modular design and encapsulation make additional attributes and method modification straightforward to integrate and maintain.

