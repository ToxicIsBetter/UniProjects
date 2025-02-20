import pandas as pd
import dataframe_image as dfi

# Mock data for vehicle counts
data = {
    "Location": ["Intersection A", "Intersection B", "Intersection C", "Intersection D", "Intersection E"],
    "Cars": [120, 95, 150, 130, 110],
    "Buses": [15, 10, 25, 20, 18],
    "Trucks": [30, 25, 40, 35, 28],
    "Two-wheelers": [80, 70, 100, 90, 85]
}

# Create a DataFrame
vehicle_counts_df = pd.DataFrame(data)

# Save the DataFrame as a PNG image
dfi.export(vehicle_counts_df, 'vehicle_counts_table.png')