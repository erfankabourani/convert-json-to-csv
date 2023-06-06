import json

if __name__ == '__main__':
    try:
        # Attempt to open and read the JSON file
        with open('input.json', 'r') as f:
            data = json.loads(f.read())

        # Extract the keys from the first object and join them with commas
        output = ','.join([*data[0]])

        # Iterate over each object in the data
        for obj in data:
            # Append name, age, and birthday values to the output string with formatting
            output += f'\n{obj["name"]} , {obj["age"]} , {obj["birthday"]}'

        # Write the output string to a CSV file
        with open('output.csv', 'w') as f:
            f.write(output)

    except Exception as ex:
        # Catch any exceptions that occur and print an error message
        print(f'Error: {str(ex)}')
