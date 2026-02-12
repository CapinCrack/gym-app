import streamlit as st
import pandas as pd
import os

# ----------- File setup ----------
DATA_FILE = "lifts.csv"

# Load existing data
if os.path.exists(DATA_FILE):
    df_lifts = pd.read_csv(DATA_FILE)
else:
    df_lifts = pd.DataFrame(columns=["Username", "Age", "Height", "Experience", "Exercise", "Weight", "Reps"])

# ----------- Page setup ----------
st.set_page_config(
    page_title="Gym Stats",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Gym Stats MVP")

# ----------- Sidebar ----------
st.sidebar.header("Your Profile")
username = st.sidebar.text_input("Username")
age = st.sidebar.number_input("Age", min_value=12, max_value=100, value=20)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170)
experience = st.sidebar.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# ----------- Tabs ----------
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    username = st.text_input("Username")

with col2:
    age = st.number_input("Age", min_value=12, max_value=100, value=20)

with col3:
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)

with col4:
    exercise = st.selectbox(
        "Exercise",
        ["Bench Press", "Squat", "Deadlift", "Overhead Press"]
    )

with col5:
    weight = st.number_input("Weight (kg)", min_value=1, max_value=500, value=50)

with col6:
    reps = st.number_input("Reps", min_value=1, max_value=20, value=5)

if st.button("Add Lift"):
    if "lifts" not in st.session_state:
        st.session_state.lifts = []
    
    st.session_state.lifts.append({
        "Username": username,
        "Age": age,
        "Height": height,
        "Exercise": exercise,
        "Weight": weight,
        "Reps": reps
    })
    st.success(f"Added {reps} reps of {weight}kg {exercise} for {username}")
