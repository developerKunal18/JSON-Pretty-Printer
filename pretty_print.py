import json

json_input = input("Enter JSON string: ")

try:
    parsed = json.loads(json_input)
    pretty = json.dumps(parsed, indent=4)
    
    print("\nFormatted JSON:\n")
    print(pretty)

except json.JSONDecodeError:
    print("Invalid JSON input")
