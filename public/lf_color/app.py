import streamlit as st
from data import (
    delta_o_cm, 
    metal_g, 
    ligand_data, 
    geometry_coord,
    )


def wavelength_nm(dq_cm: float) -> float:
    '''Convert Δ₀ in cm⁻¹ to λmax in nm.'''
    return 1e7 / dq_cm

def nm_to_rgb(nm: float) -> str:
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

def average_f (ligand_counts: dict[str, int]) -> float:
    """Donor-site-weighted average nephelauxetic factor."""
    site_sum, f_sum = 0, 0
    for lig, n_lig in ligand_counts.items():
        entry = ligand_data[lig]
        sites = n_lig * entry["dent"]
        site_sum += sites
        f_sum += sites * entry["f"]
    return f_sum / site_sum if site_sum else 1.0

st.title("Ligand Field Color Predictor (ß)")

preset_label = "— build custom complex —"
preset_choice = st.selectbox(
    "Choose a preset complex *or* build your own",
    [preset_label] + list(delta_o_cm.keys()),
)

# Preset complex
if preset_choice != preset_label:
    dq = delta_o_cm[preset_choice]
    λ_nm = wavelength_nm(dq)
    colour = nm_to_rgb(λ_nm)

    st.markdown(f"**Preset selected:** `{preset_choice}`")
    st.markdown(f"10Dq = `{dq} cm⁻¹`  →  λ<sub>max</sub> ≈ `{λ_nm:.0f} nm`")
    st.markdown(
        f"<div style='width:120px;height:50px;border:1px solid #000;"
        f"background:{colour}'></div>",
        unsafe_allow_html=True,
    )

# Custom complex builder
else:
    st.subheader("Custom complex builder")

    # metal and geometry
    metal = st.selectbox("Metal / oxidation state", list(metal_g.keys()))
    geometry = st.radio("Geometry", list(geometry_coord.keys()), horizontal=True)
    max_sites = geometry_coord[geometry]

    # ligand table
    st.markdown("#### Ligand set")
    n_rows = st.number_input("Number of different ligands", 1, 6, 1, step=1)
    ligand_counts: dict[str, int] = {}
    total_sites = 0

    for i in range(int(n_rows)):
        col1, col2 = st.columns([3, 1])
        with col1:
            lig = st.selectbox(
                f"Ligand {i + 1}", list(ligand_data.keys()), key=f"lig_{i}"
            )
        with col2:
            cnt = st.number_input(
                "count", 0, 6, step=1, key=f"cnt_{i}"
            )
        ligand_counts[lig] = int(cnt)
        total_sites += ligand_data[lig]["dent"] * int(cnt)

    # live validation
    if total_sites > max_sites:
        st.error(
            f"Total donor sites = {total_sites} exceeds "
            f"{max_sites} for {geometry}."
        )
    elif total_sites < max_sites:
        st.warning(
            f"{max_sites - total_sites} open coordination sites remain."
        )
    else:
        st.success("Coordination number satisfied.")

    # submit button
    can_submit = (total_sites == max_sites) and any(ligand_counts.values())
    submit = st.button("Compute colour", disabled=not can_submit)

    # calculation
    if submit:
        f_bar = average_f(ligand_counts)
        B_free = metal_g[metal]          # cm‑1
        B_eff  = B_free * f_bar
        dq_cm  = 10.5 * B_eff            # empirical Δ = k·B ; k≈10–12
        λ_nm   = wavelength_nm(dq_cm)
        colour = nm_to_rgb(λ_nm)

        st.markdown(
            f"**Metal:** {metal} &nbsp; | &nbsp; **Geometry:** {geometry}"
        )
        st.markdown(
            f"10Dq ≈ `{dq_cm:.0f} cm⁻¹`  →  λ<sub>max</sub> ≈ `{λ_nm:.0f} nm`"
        )
        st.markdown(
            f"<div style='width:120px;height:50px;border:1px solid #000;"
            f"background:{colour}'></div>",
            unsafe_allow_html=True,
        )
