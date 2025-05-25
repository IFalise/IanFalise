delta_o_cm = {
    "[Ti(H2O)6]3+": 20300,
    "[V(H2O)6]2+": 12600,
    "[V(H2O)6]3+": 18900,
    "[Cr(H2O)6]2+": 13900,
    "[CrCl6]3-": 13000,
    "[Cr(H2O)6]3+": 17400,
    "[Cr(NH3)6]3+": 21500,
    "[Cr(CN)6]3-": 26600,
    "Cr(CO)6": 34150,
    "[MnCl6]4-": 7500,
    "[Mn(H2O)6]2+": 8500,
    "[MnCl6]3-": 20000,
    "[Mn(H2O)6]3+": 21000,
    "[Fe(H2O)6]2+": 10400,
    "[Fe(H2O)6]3+": 14300,
    "[Fe(CN)6]4-": 32800,
    "[Fe(CN)6]3-": 35000,
    "[CoF6]3-": 13000,
    "[Co(H2O)6]2+": 9300,
    "[Co(H2O)6]3+": 27000,
    "[Co(NH3)6]3+": 22900,
    "[Co(CN)6]3-": 34800,
    "[Ni(H2O)6]2+": 8500,
    "[Ni(NH3)6]2+": 10800,
    "[RhCl6]3-": 20400,
    "[Rh(H2O)6]3+": 27000,
    "[Rh(NH3)6]3+": 34000,
    "[Rh(CN)6]3-": 45500,
    "[IrCl6]3-": 25000,
    "[Ir(NH3)6]3+": 41000,
}

ligand_data = {
    "Br-": {"f": 0.72, "dent": 1},
    "(SCN)-": {"f": 0.75, "dent": 1},
    "Cl-": {"f": 0.78, "dent": 1},
    "OPCl3": {"f": 0.82, "dent": 1},
    "(N3)-": {"f": 0.83, "dent": 1},
    "F-": {"f": 0.90, "dent": 1},
    "(OSMe3)-": {"f": 0.91, "dent": 1},
    "OCMe2": {"f": 0.92, "dent": 1},
    "EtOH": {"f": 0.97, "dent": 1},
    "Me2NCHO": {"f": 0.98, "dent": 1},
    "(C2O4)2-": {"f": 0.99, "dent": 2},            # oxalate, O,O‑bidentate
    "H2O": {"f": 1.00, "dent": 1},
    "SC(NH2)2": {"f": 1.01, "dent": 1},
    "NCS-": {"f": 1.02, "dent": 1},
    "NCSe-": {"f": 1.03, "dent": 1},
    "(NH2CH2CO2)-": {"f": 1.18, "dent": 2},        # glycinate, N,O‑bidentate
    "CH3CN": {"f": 1.22, "dent": 1},
    "C5H5": {"f": 1.23, "dent": 1},                # η5‑Cp treated as one site
    "NH3": {"f": 1.25, "dent": 1},
    "en": {"f": 1.28, "dent": 2},                  # ethylenediamine, N,N‑bidentate
    "(SO3)2-": {"f": 1.20, "dent": 2},             # sulfite, O,O‑bidentate
    "diars": {"f": 1.33, "dent": 2},               # diarsine, As,As‑bidentate
    "bipy": {"f": 1.33, "dent": 2},                # 2,2′‑bipyridine, N,N‑bidentate
    "(NO2)-": {"f": 1.40, "dent": 1},
    "CN-": {"f": 1.70, "dent": 1},
}

metal_g = {
    "Mn2+": 8000,
    "Ni2+": 8700,
    "Co2+": 9000,
    "V2+": 12000,
    "Fe3+": 14000,
    "Cu3+": 15700,
    "Cr3+": 17400,
    "Co3+": 18200,
    "Ru2+": 20000,
    "Ag3+": 20400,
    "Ni4+": 22000,
    "Mn4+": 24000,
    "Mo3+": 24600,
    "Rh3+": 27000,
    "Mn2+": 8000,
    "Tc4+": 31000,
    "Ir3+": 8000,
    "Pt4+": 36000,
    "Fe2+": 8500,

}

geometry_coord = {
    "Octahedral": 6,
    "Tetrahedral": 4,
    "Square-Pyramidal": 5,
    "Trigonal-Bipyramidal": 5,
    "Square-Planar": 4,
    "Trigonal-Planar": 3,
    "Linear": 2,
}
