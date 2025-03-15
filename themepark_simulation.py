import pandas as pd
from Themepark_classes import Ride, ThemePark

ride_info = pd.read_csv("ride_info.csv")
arrival_rates = pd.read_csv("arrival_rates.csv")
ride_transitions = pd.read_csv("ride_transitions.csv", header=0)  
transition_matrix = ride_transitions.to_numpy()  # Convert DataFrame to numpy array

# Prepare a list of rides based on ride_info.csv
rides = []
for _, row in ride_info.iterrows(): 
    ride_id = row['ride_id']
    ride_name = row['ride_name']
    ride_rate = row['service_rate']
    rides.append(Ride(ride_id, ride_name, ride_rate))

results = []  # List to store simulation results

# Run simulations for each row in arrival_rates
for index, row in arrival_rates.iterrows():
    arrival_rate = row['arrival_rate']
    day = row['day']
    week = row['week']
    themepark = ThemePark(rides, arrival_rate, transition_matrix)
    themepark.simulate(max_time=10)

    for customer in themepark.customers:
        # Create a dictionary, keys are column names, values are the corresponding data for each customer
        result_row = {
            'customer_id': customer.customer_id,
            'n_rides': len(customer.path),
            'wait_time': sum(customer.wait_times),
            'ride_time': sum(customer.ride_times),
            'arrival_rate': arrival_rate,
            'day': day,
            'week': week
        }
        results.append(result_row)  # results is now a list of dictionaries

# Convert the list results into a pandas dataframe and save it to a CSV file
results_df = pd.DataFrame(results)
results_df.to_csv("simulations_output.csv", index=False)
