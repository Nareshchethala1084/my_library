import requests
import json
import pandas as pd

def fetch_data(url, params=None):
    """Fetch data from the specified URL with optional parameters."""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()  # Returns the response as a JSON object
    except requests.RequestException as e:
        print(f"Error fetching data: {str(e)}")
        return None

def save_data_to_json(data, filename):
    """Save data to a JSON file."""
    try:
        with open(filename + '.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}.json")
    except IOError as e:
        print(f"Error saving file: {str(e)}")

def save_data_to_csv(data, filename):
    """Save data to a CSV file."""
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename + '.csv', index=False)
        print(f"Data saved to {filename}.csv")
    except Exception as e:
        print(f"Error processing or saving CSV: {str(e)}")

def save_data_to_excel(data, filename):
    """Save data to an Excel file."""
    try:
        df = pd.DataFrame(data)
        df.to_excel(filename + '.xlsx', index=False)
        print(f"Data saved to {filename}.xlsx")
    except Exception as e:
        print(f"Error processing or saving Excel file: {str(e)}")

def main():
    # User inputs
    url = input("Enter the URL of the API endpoint: ")
    params_input = input("Enter query parameters (key=value), separated by commas (e.g., key1=value1,key2=value2), or press enter if none: ")
    filename = input("Enter the filename without extension where you want to save the file: ")
    format_choice = input("Enter the desired format (json, csv, excel): ").lower()

    # Parse user input into dictionary for parameters if provided
    params = {}
    if params_input:
        try:
            params = dict(x.split('=') for x in params_input.split(','))
        except ValueError:
            print("Error parsing parameters. Please ensure they are in key=value format.")
            return

    # Fetch data
    data = fetch_data(url, params)
    if data is not None:
        # Save the data based on the user's choice of format
        if format_choice == 'csv':
            save_data_to_csv(data, filename)
        elif format_choice == 'excel':
            save_data_to_excel(data, filename)
        else:
            save_data_to_json(data, filename)

if __name__ == "__main__":
    main()
