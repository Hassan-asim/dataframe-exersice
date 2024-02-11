import pandas as pd

# Define the file path
file_path = "H:\\AICP INTERNSHIP\\EDA\\week 2\\EDA Internship 2.0 Week 2\\people.csv"

# Read the CSV file, selecting specific columns and skipping rows 1 and 5
df = pd.read_csv(file_path, usecols=["First Name", "Sex", "Email", "Phone", "Job Title"], skiprows=[1, 5])

# Set the specified columns as index
df.set_index(["Sex", "Job Title"], inplace=True)

# Export the DataFrame to a new CSV file
df.to_csv("H:\\AICP INTERNSHIP\\EDA\\week 2\\EDA Internship 2.0 Week 2\\Newpeople.csv")
