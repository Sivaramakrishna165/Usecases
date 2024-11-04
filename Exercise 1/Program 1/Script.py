# Python script that sorts the given JSON array by the height attribute:
import json

# Sample input JSON array
input_data = [
    {"name": "Person1", "height": 158},
    {"name": "Person2", "height": 174},
    {"name": "Person3", "height": 146}
]

# Sorting the JSON array by the height attribute
sorted_data = sorted(input_data, key=lambda x: x["height"])

# Printing the sorted result
print(json.dumps(sorted_data, indent=4))
