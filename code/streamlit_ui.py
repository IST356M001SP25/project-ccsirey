import streamlit as st
from bart_stations import bart_stations 
from apicalls import get_directions

st.set_page_config(page_title="BART Travel Time Comparator", layout="centered")
st.title("BART Station Travel Time Comparator")
st.write(
    "BART is the local rapid transit line serving the San Francisco Bay Area. "
    "This app compares travel times between two BART stations using Google Maps API."
    "The travel times are estimated based on current traffic conditions and may vary."
    " Please select two different BART stations from the dropdowns below."
    " The app will fetch the estimated travel times for both driving and transit modes."
)

# Dropdowns to select stations
station_from = st.selectbox("Select your starting BART station:", list(bart_stations.keys()))
station_to = st.selectbox("Select your destination BART station:", list(bart_stations.keys()))

if station_from and station_to:
    if station_from == station_to:
        st.warning("Please choose two different stations.")
    else:
        with st.spinner("Fetching travel times..."):
            try:
                driving_time = get_directions(station_from, station_to, mode="driving")
                transit_time = get_directions(station_from, station_to, mode="transit")

                st.subheader("Estimated Travel Times")
                st.write(f"**Driving:** {driving_time}")
                st.write(f"**Transit:** {transit_time}")
            except Exception as e:
                st.error(f"An error occurred: {e}")