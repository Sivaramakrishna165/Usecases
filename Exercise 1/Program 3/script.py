import csv

# Sample input JSON array
input_data = [
    {"name": "Person1", "height": 158},
    {"name": "Person2", "height": 174},
    {"name": "Person3", "height": 146}
]

# Specify the CSV file name
csv_file_name = "output.csv"

# Writing to the CSV file
with open(csv_file_name, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["name", "height"])
    writer.writeheader()  # Writing the header row
    writer.writerows(input_data)  # Writing the data rows

print(f"Data has been written to {csv_file_name}")
