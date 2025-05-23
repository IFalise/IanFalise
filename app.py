import streamlit as st
from data import delta_o_cm

def wavelength_nm(dq_cm):
    """Convert delta q in cm^-1 to wavelength in nm."""
    return 1e7 / dq_cm

def nm_to_rgb(nm):
    """Visual mapping of 380-750 nm -> Hex color."""
    bands = [
        (380, 400, "#6D007E"), 
        (400, 420, "#6700B4"),
        (420, 440, "#3700E6"),
        (440, 460, "#0046FF"),
        (460, 480, "#00A9FF"),
        (480, 500, "#00FFFF"),
        (500, 520, "#00FF00"),
        (520, 540, "#5DFF00"),
        (540, 560, "#A2FF00"),
        (560, 580, "#E1FF00"),
        (580, 600, "#FFDF00"),
        (600, 620, "#FF9B00"),
        (620, 640, "#FF4E00"), 
        (640, 660, "#F80000"),
        (660, 680, "#DC0000"),
        (680, 700, "#BF0000"),
        (700, 720, "#A10000"),
        (720, 740, "#820000"),
    ]

    for lo, hi, hexcode in bands:
        if lo <= nm < hi:
            return hexcode
    return "#808080"

st.title("Ligand Field Color Predictor (ß)")

complex_name = st.selectbox("Choose a complex", list(delta_o_cm.keys()))

dq = delta_o_cm[complex_name]
lamb = wavelength_nm(dq)
hexcolor = nm_to_rgb(lamb)

st.markdown(f"**Δ₀** = `{dq} cm⁻¹` → **λmax** ≈ `{lamb:.0f} nm`")
st.markdown(
    f"<div style='width: 120px; height: 50px; border: 1px solid #000;"
    f"background: {hexcolor}'</div>;",
    unsafe_allow_html=True
)

if st.button("Copy λ to clipboard"):
    st.write("'λ' copy-paste it into your notebook!")

    