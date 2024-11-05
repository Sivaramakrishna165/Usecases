Explanation:

Schema Definition:

1. The schema specifies that the input is an array of objects.
2. Each object must have name (a string) and height (an integer) as required properties.
3. additionalProperties: False ensures no extra fields are allowed in the objects.
   
Validation Function:

1. jsonschema.validate() is used to validate the input data against the defined schema.
   
2. If the data does not match the schema, a ValidationError is raised.
   
Input :

[{"name": "Person1", "height": 158}, {"name": "Person2", "height": "174"}, {"name": 123, "height": 174}, {"name": "Person3", "height": 167},{"name": 123, "height": "174"}]

Output:

Validating input data:
Validation errors:
 - Error in item at index 1
   - Error message: '174' is not of type 'integer'
   - Invalid data: 174
   - Path to error: 1/height

 - Error in item at index 2
   - Error message: 123 is not of type 'string'
   - Invalid data: 123
   - Path to error: 2/name

 - Error in item at index 4
   - Error message: 123 is not of type 'string'
   - Invalid data: 123
   - Path to error: 4/name

 - Error in item at index 4
   - Error message: '174' is not of type 'integer'
   - Invalid data: 174
   - Path to error: 4/height
   
This script demonstrates both successful validation and failures, proving that the schema validation works correctly.
