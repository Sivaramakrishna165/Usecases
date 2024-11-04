# Python script to validate the JSON data using the schema
import json
import jsonschema
from jsonschema import validate

# Define the JSON schema
schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "height": {"type": "integer"}
        },
        "required": ["name", "height"],
        "additionalProperties": False
    }
}

# Sample input JSON array (valid data)
valid_input_data = [
    {"name": "Person1", "height": 158},
    {"name": "Person2", "height": 174},
    {"name": "Person3", "height": 146}
]

# Sample input JSON array (invalid data for testing negative cases)
invalid_input_data = [
    {"name": "Person1", "height": "158"},  # Height is a string, not an integer
    {"name": 123, "height": 174},          # Name is a number, not a string
    {"height": 146}                        # Missing the 'name' field
]

# Function to validate JSON data against the schema
def validate_json(data):
    try:
        validate(instance=data, schema=schema)
        print("Validation passed!")
    except jsonschema.exceptions.ValidationError as err:
        print(f"Validation error: {err.message}")

# Validate the valid input data
print("Validating valid input data:")
validate_json(valid_input_data)

# Validate the invalid input data
print("\nValidating invalid input data:")
validate_json(invalid_input_data)
