import streamlit as st
import plotly.express as px
from dataprocess import get_data
from datetime import datetime


# Set the title for the Streamlit app
st.title("Weather Forecast for the Next Days")

# Create a text input field for the user to enter the place
place = st.text_input("Place")

# Create a slider for the user to select the number of forecast days (1 to 5 days)
day = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Slider to select the number of days to forecast.")

# Create a selectbox for the user to choose between viewing temperature or sky conditions
view_by = st.selectbox("Select data to view", ("Temperature", "Sky"))

# Display a subheader indicating the chosen view, number of days, and place
st.subheader(f"{view_by} for the next {day} days in {place}")

# Check if the user has entered a place
if place:
    # Attempt to get filtered weather data based on the user's input place and number of forecast days

    try:
        filtered_data = get_data(place, day)

        # Check if the user chose to view temperature data
        if view_by == "Temperature":
            # Extract temperature data and dates from the filtered data
            temperature = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]

            # Create a line chart using Plotly with temperature data and dates
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature(c)"})

            # Display the line chart in the Streamlit app
            st.plotly_chart(figure)

        if view_by == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}

            # Extract date, time, description, and sky conditions
            date_time_description_sky = [
                (dict['dt_txt'], dict['weather'][0]['description'], dict['weather'][0]['main'])
                for dict in filtered_data
            ]

            # Specify the number of columns for display
            num_columns = 4

            # Calculate the number of items per column
            items_per_column = len(date_time_description_sky) // num_columns

            # Create multiple columns
            columns = st.columns(num_columns)

            # Iterate through the data and display in columns
            for i in range(num_columns):
                with columns[i]:
                    for j in range(i * items_per_column, (i + 1) * items_per_column):
                        if j < len(date_time_description_sky):
                            date_time, description, condition = date_time_description_sky[j]
                            date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
                            st.write(date_time.strftime("%A, %B %d, %Y %I:%M %p"))
                            st.write(f"Condition: {description.title()}")
                            st.image(images[condition], width=115)
    # Handle the KeyError exception, which is raised if the 'place' does not exist in the API response
    except KeyError:
        # Display a message using Streamlit indicating that the specified place does not exist
        st.write("Place does not exists")
        