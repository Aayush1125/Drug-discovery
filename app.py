import streamlit as st
from PIL import Image
import os

# Hardcoded data per compound
compounds = {
    "Imatinib": {
        "fp_shap": "shap_images/Imatinib_fp.png",
        "bonds": "shap_images/Imatinib_bonds.png",
        "desc_shap": "shap_images/Imatinib_desc.png",
        "kinase": "- Mast/stem cell growth factor receptor Kit"
    },
    "NERATINIB": {
        "fp_shap": "shap_images/NERATINIB_fp.png",
        "bonds": "shap_images/NERATINIB_bonds.png",
        "desc_shap": "shap_images/NERATINIB_desc.png",
        "kinase": (
            "- EGFR (Epidermal growth factor receptor)\n"
            "- ERBB2 (Receptor tyrosine-protein kinase erbB-2)"
        )
    },
    "SITAGLIPTIN": {
        "fp_shap": "shap_images/SITAGLIPTIN_fp.png",
        "bonds": "shap_images/SITAGLIPTIN_bonds.png",
        "desc_shap": "shap_images/SITAGLIPTIN_desc.png",
        "kinase": "- Dipeptidyl peptidase 4 (DPP-4)"
    },
    "SUNITINIB": {
        "fp_shap": "shap_images/SUNITINIB_fp.png",
        "bonds": "shap_images/SUNITINIB_bonds.png",
        "desc_shap": "shap_images/SUNITINIB_desc.png",
        "kinase": (
            "- KIT – Stem cell factor receptor (CD117)\n"
            "- FLT3 – Fms-like tyrosine kinase 3"
        )
    }
}

st.set_page_config(page_title="Compound SHAP & Bonds Viewer", layout="wide")

st.title("🧪 Compound SHAP & Bond Interpretation Dashboard")

compound = st.selectbox("Select a compound", list(compounds.keys()))
view = st.radio("Select analysis type", ["Fingerprint SHAP & Bond Highlighting", "Descriptor SHAP & Kinase Targets"])

compound_data = compounds[compound]

if view == "Fingerprint SHAP & Bond Highlighting":
    st.subheader(f"{compound} – Fingerprint SHAP Values")
    st.image(compound_data["fp_shap"], caption="Fingerprint SHAP Summary", use_column_width=True)

    st.subheader("Highlighted Bonds from Morgan Fingerprint Bits")
    st.image(compound_data["bonds"], caption="Top contributing Morgan fingerprint bits", use_column_width=True)

elif view == "Descriptor SHAP & Kinase Targets":
    st.subheader(f"{compound} – Descriptor SHAP Values")
    st.image(compound_data["desc_shap"], caption="Descriptor SHAP Summary", use_column_width=True)

    st.subheader("🧬 Kinase Targets")
    st.code(compound_data["kinase"])
