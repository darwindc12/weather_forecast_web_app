# Weather Forecast
This code uses the streamlit and plotly.express libraries to create a weather forecast application that allows users to input a location and view the forecast for the next 1-5 days. The user can also choose to view the forecast by temperature or sky condition. The get_data function from the dataprocess module is used to filter the data according to the user's input.

# Setup
- Make sure you have the streamlit, plotly, and requests libraries installed by running pip install streamlit plotly requests in your command line.
- You need to have an OpenWeatherMap API key. Sign up for a free key from https://openweathermap.org/price and replace the get_data() function with your own function to get the forecast data from the OpenWeatherMap API.

# Usage
- Run the script using streamlit run weather_forecast.py.
- In the text box, enter a location for which you want to see the forecast.
- Use the slider to choose the number of days for which you want to see the forecast.
- Select whether you want to see the forecast by temperature or sky condition.
- The forecast will be displayed based on your choices.
- If the location does not exist, an error message will be displayed.
