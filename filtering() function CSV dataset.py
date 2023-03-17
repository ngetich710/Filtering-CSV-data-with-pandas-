# Load the Pandas libraries with alias 'pd' 
import pandas as pd
#read CSV file
df = pd.read_csv('athlete_events.csv')

## Calling the filtering function
def filtering(dataframe):
    # Load the CSV file as a DataFrame
    df = pd.read_csv("athleteevents.csv")
    
    num_records, filtered_df = filtering(df)

    # this asks the user which features to use as filters
    valid_options = set(range(1, 2**len(dataframe.columns)))  
    # valid options are binary numbers from 1 to 2^num_features - 1
    while True:
        option_str = input(f"Enter a number with up to {len(dataframe.columns)} digits to select features to filter (e.g. 123): ")
        try:
            option = int(option_str)
        except ValueError:
            print("Invalid input. Please enter a number with digits from 1 to 5.")
            continue
        if option not in valid_options:
            print("Invalid input. Please enter a number with digits from 1 to 5.")
            continue
        break
    
    # Parse the selected features from the binary representation of the option
    selected_features = []
    for i, col in enumerate(dataframe.columns):
        if option & (2**i):
            selected_features.append(col)
    
    # Ask the user for the filter values for each selected feature
    filter_values = {}
    for feature in selected_features:
        filter_value = input(f"Enter a value for {feature}: ")
        filter_values[feature] = filter_value
    
    # Apply the filters and return the results
    filtered_data = dataframe.copy()
    for feature, value in filter_values.items():
        filtered_data = filtered_data[filtered_data[feature] == value]
    
    return len(filtered_data), filtered_data






