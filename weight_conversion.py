import streamlit as st

st.set_page_config(page_title="Weight Conversion", page_icon="⚖️")

st.title("⚖️ Weight Conversion Calculator")

st.write("Convert between Mass (kg), Force (N), and Force (kN)")

kg = st.text_input("Mass (kg)")
n = st.text_input("Force (N)")
kn = st.text_input("Force (kN)")

if st.button("Calculate"):
    filled = sum(bool(x.strip()) for x in [kg, n, kn])

    if filled == 0:
        st.error("Please enter a value in one field.")
    elif filled > 1:
        st.error("Please enter a value in only one field.")
    else:
        try:
            if kg:
                kg_val = float(kg)
                n_val = kg_val * 9.81
                kn_val = n_val / 1000

            elif n:
                n_val = float(n)
                kg_val = n_val / 9.81
                kn_val = n_val / 1000

            elif kn:
                kn_val = float(kn)
                n_val = kn_val * 1000
                kg_val = n_val / 9.81

            st.success("Conversion Results")

            st.write(f"**Mass (kg):** {kg_val:.2f}")
            st.write(f"**Force (N):** {n_val:.2f}")
            st.write(f"**Force (kN):** {kn_val:.2f}")

        except ValueError:
            st.error("Please enter a valid numeric value.")

if st.button("Reset"):
    st.rerun()