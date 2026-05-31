import streamlit as st

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
    st.rerun()


# --------------------------------------------------
# CONVERSION FACTORS TO NEWTON
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
# PAGE TITLE
# --------------------------------------------------
st.markdown(
    """
    <h1 style='text-align:center;'>
        ⚖️ Weight Conversion
    </h1>
    """,
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
        options=list(TO_NEWTON.keys()),
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

    html = """
    <table style="
        width:100%;
        border-collapse:collapse;
        font-family:Arial, sans-serif;
        font-size:15px;
    ">
        <tr>
            <th style="
                border:1px solid #d0d0d0;
                padding:10px;
                text-align:center;
                background-color:#f2f2f2;
            ">
                Unit
            </th>

            <th style="
                border:1px solid #d0d0d0;
                padding:10px;
                text-align:center;
                background-color:#f2f2f2;
            ">
                Value
            </th>
        </tr>
    """

    for unit, value in st.session_state.results.items():

        html += f"""
        <tr>
            <td style="
                border:1px solid #d0d0d0;
                padding:8px 12px;
                text-align:left;
            ">
                {unit}
            </td>

            <td style="
                border:1px solid #d0d0d0;
                padding:8px 12px;
                text-align:right;
                font-family:Consolas, monospace;
            ">
                {value:,.2f}
            </td>
        </tr>
        """

    html += "</table>"

    st.markdown(html, unsafe_allow_html=True)