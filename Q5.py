import pandas as pd

# Create a dictionary with column names as keys and lists of data as values
data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['rain', 'sunny', 'snow', 'snow', 'rain', 'sunny']
}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Calculate mean, maximum, and minimum for the 'temperature' column
temperature_mean = df['temperature'].mean()
temperature_max = df['temperature'].max()
temperature_min = df['temperature'].min()

# Display the DataFrame
print(df)

# Display the results
print("Mean Temperature:", temperature_mean)
print("Maximum Temperature:", temperature_max)
print("Minimum Temperature:", temperature_min)
