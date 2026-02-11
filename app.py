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
st.set_page_config(page_title="Gym Stats MVP", layout="wide")
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
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Log Lift", "Your Lifts", "Compare", "Stats", "Goals"])

# ----------- Log lifts ----------
with tab1:
    st.header("Log a Lift")
    exercise = st.selectbox(
        "Exercise",
        ["Bench Press", "Squat", "Deadlift", "Overhead Press"]
    )
    weight = st.number_input("Weight (kg)", min_value=1, max_value=500, value=50)
    reps = st.number_input("Reps", min_value=1, max_value=20, value=5)

    if st.button("Add Lift"):
        if not username:
            st.warning("Please enter your username first!")
        else:
            new_lift = {
                "Username": username,
                "Age": age,
                "Height": height,
                "Experience": experience,
                "Exercise": exercise,
                "Weight": weight,
                "Reps": reps
            }
            df_lifts = pd.concat([df_lifts, pd.DataFrame([new_lift])], ignore_index=True)
            df_lifts.to_csv(DATA_FILE, index=False)
            st.success(f"Added {reps} reps of {weight}kg {exercise}")

# ----------- Show logged lifts (your lifts only) ----------
with tab2:
    st.header("Your Logged Lifts")
    if username and not df_lifts[df_lifts["Username"] == username].empty:
        st.dataframe(df_lifts[df_lifts["Username"] == username])
    else:
        st.info("No lifts logged yet")

# ----------- Compare (all users) ----------
with tab3:
    st.header("Compare With Others")
    if not df_lifts.empty:
        df = df_lifts.copy()

        # Calculate simple percentile
        def percentile(weight, exercise):
            max_weights = {
                "Bench Press": 200,
                "Squat": 250,
                "Deadlift": 300,
                "Overhead Press": 150
            }
            return round((weight / max_weights.get(exercise, 1)) * 100, 1)

        df["Percentile"] = df.apply(lambda row: percentile(row["Weight"], row["Exercise"]), axis=1)
        st.dataframe(df[["Username", "Exercise", "Weight", "Reps", "Percentile"]])
    else:
        st.info("No lifts logged yet")
# ----------- Stats ----------
with tab4:
    st.header("Stats")
    st.write("Coming Soon")
# ----------- Goals ----------
with tab5:
    st.header("My Goals")
    st.write("Coming Soon")
