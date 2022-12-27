import requests

API_KEY = "76df065c44fd5994d2e9424a48fd90f4"


def get_data(place, day=None, view_by=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    data_filtered = data['list']
    nd = 8 * day
    data_filtered = data_filtered[:nd]
    if view_by == 'Temperature':
        data_filtered = [dict['main']['temp'] for dict in data_filtered]
    if view_by == 'Sky':
        data_filtered = [dict['weather'][0]['main'] for dict in data_filtered]
    return data_filtered


if __name__ == "__main__":
    print(get_data(place="Tokyo", day=2,  view_by='Temperature'))