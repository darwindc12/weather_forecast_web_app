import streamlit as st
import plotly.express as px
from dataprocess import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
day = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Slider to select number days to forecast.")
view_by = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))
st.subheader(f"{view_by} for the next {day} days in {place}")



if place:
    
    filtered_data = get_data(place, day)

    if view_by == "Temperature":
        temperature = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature(c)"})
        st.plotly_chart(figure)

    if view_by == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky = [dict['weather'][0]['main'] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky]
        st.image(image_paths, width=115)
        