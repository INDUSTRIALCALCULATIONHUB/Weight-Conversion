import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Weight Conversion",
    page_icon="⚙️",
    layout="centered"
)

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

if "input_unit" not in st.session_state:
    st.session_state.input_unit = "kg"

if "results" not in st.session_state:
    st.session_state.results = None


# --------------------------------------------------
# Reset Function
# --------------------------------------------------
def reset_fields():
    st.session_state.input_value = ""
    st.session_state.input_unit = "kg"
    st.session_state.results = None


# --------------------------------------------------
# Conversion Factors to Newton
# --------------------------------------------------
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


# --------------------------------------------------
# Page Heading
# --------------------------------------------------
st.markdown(
    "<h1 style='text-align:center;'>⚙️ Weight Conversion</h1>",
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# Input Section
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
# Buttons
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
# Calculation
# --------------------------------------------------
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

        st.session_state.results = {
            "Kilogram (kg)": newton / 9.81,
            "Newton (N)": newton,
            "Kilonewton (kN)": newton / 1000,
            "Metric Ton (t)": newton / 9810,
            "Pound (lb)": newton / 4.448221615,
            "Kip": newton / 4448.221615,
            "Kilogram-force (kgf)": newton / 9.80665,
            "Ton-force (tf)": newton / 9806.65
        }

    except ValueError:
        st.error("Please enter a valid numeric value.")

# --------------------------------------------------
# Results
# --------------------------------------------------
if st.session_state.results:

    st.subheader("Conversion Results")

    html = """
    <style>
    .result-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 15px;
    }

    .result-table th {
        border: 1px solid #d0d0d0;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        background-color: #f5f5f5;
    }

    .result-table td {
        border: 1px solid #d0d0d0;
        padding: 10px;
    }

    .unit-col {
        text-align: left;
    }

    .value-col {
        text-align: right;
        font-family: Consolas, monospace;
    }
    </style>

    <table class="result-table">
        <tr>
            <th>Unit</th>
            <th>Value</th>
        </tr>
    """

    for unit, value in st.session_state.results.items():

        html += f"""
        <tr>
            <td class="unit-col">{unit}</td>
            <td class="value-col">{value:,.2f}</td>
        </tr>
        """

    html += "</table>"

    st.markdown(html, unsafe_allow_html=True)