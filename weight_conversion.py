import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Weight Conversion Calculator",
    page_icon="⚖️",
    layout="centered"
)

# -----------------------------
# Session State Initialization
# -----------------------------
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

if "input_unit" not in st.session_state:
    st.session_state.input_unit = "kg"

if "results" not in st.session_state:
    st.session_state.results = None


# -----------------------------
# Reset Function
# -----------------------------
def reset_fields():
    st.session_state.input_value = ""
    st.session_state.input_unit = "kg"
    st.session_state.results = None


# -----------------------------
# Title
# -----------------------------
st.title("⚖️ Weight Conversion Calculator")

st.markdown(
    """
Convert between:

- Kilogram (kg)
- Newton (N)
- Kilonewton (kN)
- Metric Ton (t)
- Pound (lb)
- Kip
- Kilogram-force (kgf)
- Ton-force (tf)
"""
)

# -----------------------------
# Conversion Factors to Newton
# -----------------------------
to_newton = {
    "kg": 9.81,
    "N": 1.0,
    "kN": 1000.0,
    "Metric Ton": 9810.0,
    "lb": 4.448221615,
    "kip": 4448.221615,
    "kgf": 9.80665,
    "tf": 9806.65
}

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.text_input(
        "Enter Value",
        key="input_value",
        placeholder="Enter value"
    )

with col2:
    st.selectbox(
        "Input Unit",
        list(to_newton.keys()),
        key="input_unit"
    )

# -----------------------------
# Buttons
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    calculate = st.button(
        "Calculate",
        use_container_width=True
    )

with col2:
    reset = st.button(
        "Reset",
        use_container_width=True,
        on_click=reset_fields
    )

# -----------------------------
# Calculation
# -----------------------------
if calculate:

    if st.session_state.input_value.strip() == "":
        st.error("Please enter a value.")
        st.stop()

    try:
        input_value = float(st.session_state.input_value)

        # Convert entered unit to Newton
        newton = input_value * to_newton[
            st.session_state.input_unit
        ]

        # Convert Newton to all units
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

# -----------------------------
# Display Results
# -----------------------------
if st.session_state.results:

    st.subheader("Conversion Results")

    df = pd.DataFrame({
        "Unit": list(st.session_state.results.keys()),
        "Value": [
            f"{v:,.6f}"
            for v in st.session_state.results.values()
        ]
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

# -----------------------------
# Formula
# -----------------------------
st.markdown("---")

st.markdown(
    """
### Formula Used

Force = Mass × Gravity

Gravity = 9.81 m/s²

Example:

1 kg = 9.81 N

1 kN = 1000 N
"""
)