import pandas as pd

# Define the file path
file_path = "H:\\AICP INTERNSHIP\\EDA\\week 2\\EDA Internship 2.0 Week 2\\SampleWork.xlsx"

# Read the Excel file, selecting only the first and last columns and skipping row 2
df = pd.read_excel(file_path, sheet_name=0, usecols=[0, 3], skiprows=[1])

# Set row 2 as the header
df.columns = df.iloc[0]
df = df[1:]

# Export the DataFrame to a new Excel sheet
df.to_excel("H:\\AICP INTERNSHIP\\EDA\\week 2\\EDA Internship 2.0 Week 2\\NewSheet.xlsx", index=False)



