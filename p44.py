import pandas as pd

# Create Data
data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'UP', 'MP'],
    'Area': [307713, 196244, 342239, 240928, 308252],  # in sq km
    'Population': [112374333, 60439692, 68548437, 199812341, 72626809]
}

df = pd.DataFrame(data)

# a) Complete information
print("Complete State Information:")
print(df)

# b) State with largest area
print("\nState with Largest Area:")
print(df.loc[df['Area'].idxmax(), 'State'])

# c) State with largest population
print("\nState with Largest Population:")
print(df.loc[df['Population'].idxmax(), 'State'])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']

print("\nPopulation Density:")
print(df[['State', 'Density']])

# e) State with highest density
print("\nState with Highest Population Density:")
print(df.loc[df['Density'].idxmax(), 'State'])