import streamlit as st
import plotly.express as px


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
day = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Slider to select number days to forecast.")
view_by = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))
st.subheader(f"{view_by} for the next {day} days in {place}")


def get_data(day_local):
    dates = ["2022-02-06", "2022-05-01", "2022-0712"]
    temperature = [10, 11, 12]
    temperature = [day * i for i in temperature]
    return dates, temperature


d, t = get_data(day)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature(c)"})
st.plotly_chart(figure)