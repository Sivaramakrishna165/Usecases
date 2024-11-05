# Python script to validate the JSON data using the schema
import json
import jsonschema
from jsonschema import Draft7Validator

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

# Function to validate JSON data against the schema and collect all errors
def validate_json(data):
    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(data))
    
    if not errors:
        print("Validation passed!")
    else:
        print("Validation errors:")
        for error in errors:
            # Retrieve the index of the item with the error, if it exists, and adjust to a 1-based index
            item_index = error.path[0] if error.path else "unknown"
            print(f" - Error in item at index {item_index}")
            print(f"   - Error message: {error.message}")
            print(f"   - Invalid data: {error.instance}")
            print(f"   - Path to error: {'/'.join([str(x) for x in error.path])}")
            print()

# Function to get dynamic input from the user
def get_dynamic_input():
    input_data = input("Enter JSON data as a string: ")
    try:
        # Convert the input string to a Python object (list of dictionaries)
        data = json.loads(input_data)
        return data
    except json.JSONDecodeError as json_err:
        print("Invalid JSON format. Please enter a valid JSON string.")
        print(f"Error details: {json_err}")
        return None

# Main function to run the validation
def main():
    # Get dynamic input from the user
    data = get_dynamic_input()
    if data is not None:
        print("\nValidating input data:")
        validate_json(data)

# Run the main function
if __name__ == "__main__":
    main()
