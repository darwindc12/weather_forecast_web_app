import requests

# Define the API key for accessing the OpenWeatherMap API
API_KEY = "76df065c44fd5994d2e9424a48fd90f4"

# Define a function to retrieve weather data for a specified place and number of days
def get_data(place, day=None, view_by=None):
    # Construct the URL for the OpenWeatherMap API request with the provided place and API key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    # Send an HTTP GET request to the API and store the response
    response = requests.get(url)

    # Parse the response data as JSON
    data = response.json()

    # Extract the 'list' field from the JSON data, which contains the weather forecasts
    data_filtered = data['list']

    # Calculate the maximum number of data points based on the specified number of days
    nd = 8 * day

    # Limit the data to the first 'nd' data points, effectively filtering by the number of days
    data_filtered = data_filtered[:nd]

    # Return the filtered weather data
    return data_filtered

# Check if this script is being run as the main program
if __name__ == "__main__":
    # Example usage of the get_data function with specified place, days, and view_by
    print(get_data(place="Tokyo", day=2, view_by='Temperature'))
