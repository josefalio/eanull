import pandas as pd

# Specify the path to your large CSV file
csv_file_path = 'large_dataset.csv'

# Create an iterator object to read the CSV file in chunks of 1000 rows
chunksize = 1000
csv_iterator = pd.read_csv(csv_file_path, chunksize=chunksize)

# Process each chunk
for chunk in csv_iterator:
    # Perform your data processing on the chunk here
    print(chunk.head())  # Example: Print the first few rows of the chunk
    # You can perform other operations like filtering, aggregation, etc.
