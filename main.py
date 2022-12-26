import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
day = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Slider to select number days to forecast.")
view_by = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{view_by} for the next {day} days in {place}")