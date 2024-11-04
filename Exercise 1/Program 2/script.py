# Sample input JSON array
input_data = [
    {"name": "Person1", "height": 158},
    {"name": "Person2", "height": 174},
    {"name": "Person3", "height": 146}
]

# Converting the JSON array into a Python dictionary
output_dict = {item["name"]: item["height"] for item in input_data}

# Printing the result
print(output_dict)
