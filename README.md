# ThemePark_Simulation_using_OOP

STAT0040 coursework project for Objected-Oriented Programming

## Introduction
This project simulates the operations of a theme park using Object-Oriented Programming (OOP) principles. The simulation helps analyze customer behavior, ride usage, and overall park performance.

## Main Python Scripts
- `Themepark_classes.py`: Custom module containing the core classes and methods for the simulation.
- `themepark_simulation.py`: Produces a new dataset of simulation output using input data from `ride_info.csv`, `arrival_rates.csv`, and `ride_transitions.csv`.
- `example_output_aggregation.py`: Summarizes the simulation output.
- `test_code.py`: Contains test codes that produce a different, verbose output each time, which visualises the simulation process. 

## Insights from the Theme Park Simulation Output
The file `summary_output.csv` generated using `example_output_aggregation.py` provides the following insights:

- By aggregating the output data from Monday to Sunday across 4 weeks, the simulation illustrates that the number of customers visiting is much higher on weekends than weekdays, and it peaks on Sundays.
- The average rides taken per customer appears lower during peak times (e.g., Sundays) and higher on days with fewer visitors (e.g., Tuesdays).
- Customers tend to spend more time waiting during peak times (from Fridays to Sundays), even though the average time they spend enjoying the rides is shorter (e.g., 0.84 hours on Sundays).

## Report on My Solutions in `Themepark_classes.py`

### Object-Oriented Programming

- **Encapsulation:** Each class bundles relevant attributes with methods that operate on the data. Getters with property decorators control read-only access to private attributes while preventing unauthorized modifications.
- **Inheritance:** The `Ride` class inherits from `deque`, reusing existing methods like `append()` and `popleft()`, and adds specialized attributes/methods, maintaining a clean interface.
- **Polymorphism:** The `Ride` class customizes the `append()` method, overriding it to perform different actions based on the data type (either `deque` or `Ride`).
- **Leveraging Existing Packages:** Using existing packages reduces redundancy in class designs.

### Data Structures for Certain Attributes

1. **PriorityQueue.queue:** Uses a list to store a sequence of immutable tuples representing events, ordered based on the first element.
2. **Customer and ThemePark Attributes:** Lists are used for attributes like `Customer.path`, `.ride_times`, `.wait_times`, and `ThemePark.customers` to allow for duplicates and easy mutability.
3. **Dictionary:** Maps each `customer_id` to their `queue_entry_times`, allowing fast retrieval when processing a customer.

### Possible Extensions to Make the Simulation More Realistic

1. **Height Restrictions:**
    - **Customer:** Add a `height` attribute.
    - **Ride:** Add a `min_height` attribute.
    - **ThemePark.simulate():** Check if the customer's height exceeds the ride's minimum height before adding them to the queue.

2. **Maximum Queue Lengths:**
    - **Ride:** Add a `max_queue_length` attribute.
    - **ThemePark:** Track and retrieve queue lengths for each `ride_id` using a dictionary.
    - **ThemePark.simulate():** Check the queue length before adding a customer. If the queue is full, route the customer to a different ride.

The modular design and encapsulation of the current four classes make it easy to integrate and maintain additional attributes and methods.


