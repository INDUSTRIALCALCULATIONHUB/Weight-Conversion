import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Weight Conversion Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Initialize session state
if "input_value" not in st.session_state:
    st.session_state.input_value = 0.0

if "input_unit" not in st.session_state:
    st.session_state.input_unit = "kg"

if "results" not in st.session_state:
    st.session_state.results = None


def reset_fields():
    st.session_state.input_value = 0.0
    st.session_state.input_unit = "kg"
    st.session_state.results = None


st.title("⚖️ Weight Conversion Calculator")

st.markdown(
    "Convert between **kg, N, kN, Metric Ton, lb, kip, kgf and tf**"
)

# Conversion factors to Newtons
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

col1, col2 = st.columns(2)

with col1:
    input_value = st.number_input(
        "Enter Value",
        min_value=0.0,
        format="%.6f",
        key="input_value"
    )

with col2:
    input_unit = st.selectbox(
        "Input Unit",
        list(to_newton.keys()),
        key="input_unit"
    )

col1, col2 = st.columns(2)

with col1:
    calculate = st.button("Calculate", use_container_width=True)

with col2:
    reset = st.button(
        "Reset",
        use_container_width=True,
        on_click=reset_fields
    )

if calculate:

    # Convert input to Newton
    newton = input_value * to_newton[input_unit]

    results = {
        "kg": newton / 9.81,
        "N": newton,
        "kN": newton / 1000,
        "Metric Ton": newton / 9810,
        "lb": newton / 4.448221615,
        "kip": newton / 4448.221615,
        "kgf": newton / 9.80665,
        "tf": newton / 9806.65
    }

    st.session_state.results = results

if st.session_state.results:

    st.subheader("Conversion Results")

    df = pd.DataFrame(
        {
            "Unit": st.session_state.results.keys(),
            "Value": [
                round(v, 6)
                for v in st.session_state.results.values()
            ]
        }
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.success("Calculation completed successfully.")

st.markdown("---")

st.markdown(
    """
    **Units Included**
    
    - kg : Kilogram
    - N : Newton
    - kN : Kilonewton
    - Metric Ton : Tonne
    - lb : Pound
    - kip : Kilopound
    - kgf : Kilogram-force
    - tf : Ton-force
    """
)