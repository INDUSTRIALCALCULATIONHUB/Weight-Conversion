import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Weight Conversion",
    page_icon="⚖️",
    layout="centered"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

if "input_unit" not in st.session_state:
    st.session_state.input_unit = "kg"

if "results" not in st.session_state:
    st.session_state.results = None


# --------------------------------------------------
# RESET FUNCTION
# --------------------------------------------------
def reset_fields():
    st.session_state.input_value = ""
    st.session_state.input_unit = "kg"
    st.session_state.results = None


# --------------------------------------------------
# CONVERSION FACTORS
# --------------------------------------------------
TO_NEWTON = {
    "kg": 9.81,
    "N": 1.0,
    "kN": 1000.0,
    "Metric Ton (t)": 9810.0,
    "Pound (lb)": 4.44822,
    "Kip": 4448.22,
    "Kilogram-force (kgf)": 9.81,
    "Ton-force (tf)": 9810.0
}

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>⚖️ Weight Conversion</h1>",
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
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

# --------------------------------------------------
# BUTTONS
# --------------------------------------------------
btn1, btn2 = st.columns(2)

with btn1:
    calculate = st.button(
        "Calculate",
        use_container_width=True
    )

with btn2:
    st.button(
        "Reset",
        use_container_width=True,
        on_click=reset_fields
    )

# --------------------------------------------------
# CALCULATION
# --------------------------------------------------
if calculate:

    try:

        if st.session_state.input_value.strip() == "":
            st.error("Please enter a value.")
            st.stop()

        value = float(st.session_state.input_value)

        newton = (
            value
            * TO_NEWTON[st.session_state.input_unit]
        )

        st.session_state.results = {
            "Kilogram (kg)": newton / 9.81,
            "Newton (N)": newton,
            "Kilonewton (kN)": newton / 1000,
            "Metric Ton (t)": newton / 9810,
            "Pound (lb)": newton / 4.44822,
            "Kip": newton / 4448.22,
            "Kilogram-force (kgf)": newton / 9.81,
            "Ton-force (tf)": newton / 9810
        }

    except ValueError:
        st.error("Please enter a valid numeric value.")

# --------------------------------------------------
# RESULTS
# --------------------------------------------------
if st.session_state.results:

    st.subheader("Conversion Results")

    df = pd.DataFrame({
        "Unit": list(st.session_state.results.keys()),
        "Value": [
            f"{v:,.2f}"
            for v in st.session_state.results.values()
        ]
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )