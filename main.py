import streamlit as st
from datetime import datetime
import pytz  # Import pytz for timezone handling

st.title("Timezone Display App")

# Define a list of available timezones (you can add more)
available_timezones = [
    "US/Pacific",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    # ... add more timezones
]

# Create checkboxes for each timezone
selected_timezones = []
for timezone in available_timezones:
    if st.checkbox(timezone):
        selected_timezones.append(timezone)

# Display selected timezones with their current time
st.header("Selected Timezones:")
for timezone in selected_timezones:
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    st.write(f"{timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")