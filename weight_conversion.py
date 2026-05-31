import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Weight Conversion",
    page_icon="⚖️",
    layout="centered"
)

# Session State Initialization
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

if "input_unit" not in st.session_state:
    st.session_state.input_unit = "kg"

if "results" not in st.session_state:
    st.session_state.results = None


# Reset Function
def reset_fields():
    st.session_state.input_value = ""
    st.session_state.input_unit = "kg"
    st.session_state.results = None


# Conversion Factors to Newtons
TO_NEWTON = {
    "kg": 9.81,
    "N": 1.0,
    "kN": 1000.0,
    "Metric Ton (t)": 9810.0,
    "Pound (lb)": 4.448221615,
    "Kip": 4448.221615,
    "Kilogram-force (kgf)": 9.80665,
    "Ton-force (tf)": 9806.65
}


# Title
st.title("Weight Conversion")

st.markdown("---")

# Input Section
col1, col2 = st.columns([2, 1])

with col1:
    st.text_input(
        "Enter Value",
        key="input_value",
        placeholder="Enter value"
    )

with col2:
    st.selectbox(
        "Unit",
        list(TO_NEWTON.keys()),
        key="input_unit"
    )

# Buttons
btn1, btn2 = st.columns(2)

with btn1:
    calculate = st.button(
        "Calculate",
        use_container_width=True
    )

with btn2:
    reset = st.button(
        "Reset",
        use_container_width=True,
        on_click=reset_fields
    )

# Calculation
if calculate:

    if st.session_state.input_value.strip() == "":
        st.error("Please enter a value.")
        st.stop()

    try:
        value = float(st.session_state.input_value)

        newton = (
            value
            * TO_NEWTON[st.session_state.input_unit]
        )

        results = {
            "Kilogram (kg)": newton / 9.81,
            "Newton (N)": newton,
            "Kilonewton (kN)": newton / 1000,
            "Metric Ton (t)": newton / 9810,
            "Pound (lb)": newton / 4.448221615,
            "Kip": newton / 4448.221615,
            "Kilogram-force (kgf)": newton / 9.80665,
            "Ton-force (tf)": newton / 9806.65
        }

        st.session_state.results = results

    except ValueError:
        st.error("Please enter a valid numeric value.")

# Display Results
if st.session_state.results:

    st.markdown("### Conversion Results")

    result_df = pd.DataFrame({
        "Unit": [
            "Kilogram (kg)",
            "Newton (N)",
            "Kilonewton (kN)",
            "Metric Ton (t)",
            "Pound (lb)",
            "Kip",
            "Kilogram-force (kgf)",
            "Ton-force (tf)"
        ],
        "Value": [
            f"{st.session_state.results['Kilogram (kg)']:,.2f}",
            f"{st.session_state.results['Newton (N)']:,.2f}",
            f"{st.session_state.results['Kilonewton (kN)']:,.2f}",
            f"{st.session_state.results['Metric Ton (t)']:,.2f}",
            f"{st.session_state.results['Pound (lb)']:,.2f}",
            f"{st.session_state.results['Kip']:,.2f}",
            f"{st.session_state.results['Kilogram-force (kgf)']:,.2f}",
            f"{st.session_state.results['Ton-force (tf)']:,.2f}"
        ]
    })

    st.table(result_df)