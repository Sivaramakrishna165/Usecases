Explanation:

Schema Definition:

1. The schema specifies that the input is an array of objects.
2. Each object must have name (a string) and height (an integer) as required properties.
3. additionalProperties: False ensures no extra fields are allowed in the objects.
   
Validation Function:

1. jsonschema.validate() is used to validate the input data against the defined schema.
2 If the data does not match the schema, a ValidationError is raised.

Output:

1. For valid_input_data: "Validation passed!"
2. For invalid_input_data: Error messages indicating what is wrong with each case, such as:
    "158" is not of type 'integer'
    123 is not of type 'string'
    'name' is a required property
   
This script demonstrates both successful validation and failures, proving that the schema validation works correctly.
