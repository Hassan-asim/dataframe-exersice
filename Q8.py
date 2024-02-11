import pandas as pd

# Create the DataFrame AICP_DF
data = {
    'Name': ['Sonia', 'Bilal', 'Hifza', 'Kabir', 'Jamiz'],
    'Age': [27, 24, 22, 32, 23],
    'Address': ['Lahore', 'Karachi', 'Sialkot', 'Peshawar', 'Lhr'],
    'Qualifications': ['Msc', 'MA', 'MCA', 'Phd', 'bcs']
}
AICP_DF = pd.DataFrame(data)
print("AICP_DF:")
print(AICP_DF)


# Select 'Name' and 'Qualifications' columns and save to df1
df1 = AICP_DF[['Name', 'Qualifications']]

# Add a new column "Height" to AICP_DF
heights = [5.1, 6.2, 5.1, 5.2, 5.1]
AICP_DF['Height'] = heights
print("AICP_DF:")
print(AICP_DF)


# Set column "Name" as the index column
AICP_DF.set_index('Name', inplace=True)
print("AICP_DF:")
print(AICP_DF)


# Retrieve row with index "Hifza"
row_hifza = AICP_DF.loc['Hifza']

# Retrieve row with index 3
row_index_3 = AICP_DF.iloc[3]

# Drop row with index "Bilal"
AICP_DF.drop(index='Bilal', inplace=True)


print("\ndf1:")
print(df1)
print("\nRow with index 'Hifza':")
print(row_hifza)
print("\nRow with index 3:")
print(row_index_3)
print("After droping row with Bilal\nAICP_DF:")
print(AICP_DF)