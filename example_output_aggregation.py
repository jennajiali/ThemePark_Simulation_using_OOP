import pandas as pd

df = pd.read_csv("example_output.csv")

days_in_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
summary_list = []  # List to store the summary metrics

# Loop through each day of the week in order
for day in days_in_order:
    day_df = df.loc[df["day"] == day]   # Filter the data for the current day
    
    # Group by week to count unique customer per same day each week
    grouped = day_df.groupby("week")["customer_id"].nunique()
    total_customers = grouped.sum() # Sum across all weeks

    rides_per_customer = day_df["n_rides"].mean()
    mean_wait_time = day_df["wait_time"].mean()
    mean_ride_time = day_df["ride_time"].mean()
    
    # Store each day's summary metrics as key:value pairs in a dictionary
    day_dict = {"Day": day,
                "Total Customers": total_customers,
                "Rides Per Customer": rides_per_customer,
                "Mean Wait Time": mean_wait_time,
                "Mean Ride Time": mean_ride_time}
    summary_list.append(day_dict)

# Create a DataFrame using this list of dictionaries to compare the results
summary = pd.DataFrame(summary_list)
summary.to_csv("summary_output.csv", index=False)