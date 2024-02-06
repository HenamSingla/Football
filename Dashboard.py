import pandas as pd
import nfl_data_py as nfl

# Initialize an empty DataFrame to store all the pbp data
all_years_pbp_data = pd.DataFrame()

for year in range(1999, 2024): 
    # Correctly pass the year as a list to comply with the function's requirements
    year_pbp_data = nfl.import_pbp_data([year])
    
    # Append the data for the current year to the cumulative DataFrame
    all_years_pbp_data = pd.concat([all_years_pbp_data, year_pbp_data], ignore_index=True)


# Display the first 5 rows
print(all_years_pbp_data.head())
# Get descriptive statistics for numeric columns
print(all_years_pbp_data.shape)

