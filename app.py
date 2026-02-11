import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gym Stats MVP", layout="wide")
st.title("💪 Gym Stats MVP")

# ----------- Sidebar ----------
st.sidebar.header("Your Profile")
username = st.sidebar.text_input("Username",'...')
age = st.sidebar.number_input("Age", min_value=12, max_value=100, value=20)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170)
experience = st.sidebar.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)

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
        if "lifts" not in st.session_state:
            st.session_state.lifts = []

        st.session_state.lifts.append({
            "Username": username,
            "Exercise": exercise,
            "Weight": weight,
            "Reps": reps
        })

        st.success(f"Added {reps} reps of {weight}kg {exercise}")

# ----------- Show logged lifts ----------
with tab2:
    if "lifts" in st.session_state and st.session_state.lifts:
        st.header("Your Logged Lifts")
        df = pd.DataFrame(st.session_state.lifts)
        st.dataframe(df)
    else:
        st.info("No lifts logged yet")

# ----------- Compare ----------
with tab3:
    if "lifts" in st.session_state and st.session_state.lifts:
        st.header("Compare With Others")

        df = pd.DataFrame(st.session_state.lifts)

        def percentile(weight, exercise):
            max_weights = {
                "Bench Press": 200,
                "Squat": 250,
                "Deadlift": 300,
                "Overhead Press": 150
            }
            return round((weight / max_weights[exercise]) * 100, 1)

        df["Percentile"] = df.apply(
            lambda row: percentile(row["Weight"], row["Exercise"]),
            axis=1
        )

        st.dataframe(df[["Username", "Exercise", "Weight", "Reps", "Percentile"]])
    else:
        st.info("Log lifts to see comparisons")
# ------------- Stats -------------
with tab4:
    st.header("My Stats")
    st.write("Coming soon!")
# ------------- Goals -------------
with tab5:
    st.header("My Goals")
    st.write("Hi TYNA!!!")
