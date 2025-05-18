import streamlit as st
from PIL import Image
import os

# Static data
compounds = {
    "Imatinib": {
        "fp_shap": "shap_images/Imatinib_fp.png",
        "desc_shap": "shap_images/Imatinib_desc.png",
        "kinase": "- Mast/stem cell growth factor receptor Kit"
    },
    "NERATINIB": {
        "fp_shap": "shap_images/NERATINIB_fp.png",
        "desc_shap": "shap_images/NERATINIB_desc.png",
        "kinase": "- EGFR (Epidermal growth factor receptor)\n- ERBB2 (Receptor tyrosine-protein kinase erbB-2)"
    },
    "SITAGLIPTIN": {
        "fp_shap": "shap_images/SITAGLIPTIN_fp.png",
        "desc_shap": "shap_images/SITAGLIPTIN_desc.png",
        "kinase": "- Dipeptidyl peptidase 4 (DPP-4)"
    },
    "SUNITINIB": {
        "fp_shap": "shap_images/SUNITINIB_fp.png",
        "desc_shap": "shap_images/SUNITINIB_desc.png",
        "kinase": "- KIT – Stem cell factor receptor (CD117)\n- FLT3 – Fms-like tyrosine kinase 3"
    }
}

st.set_page_config(page_title="Compound SHAP Viewer", layout="wide")

st.title("🔬 Compound SHAP Projection Viewer")

compound_name = st.selectbox("Select Compound", list(compounds.keys()))
view_option = st.radio("View Option", ["Fingerprint SHAP + Highlighted Bonds", "Descriptor SHAP + Kinase Info"])

compound_data = compounds[compound_name]

if view_option == "Fingerprint SHAP + Highlighted Bonds":
    st.subheader(f"{compound_name} — Fingerprint SHAP with Bond Highlighting")
    st.image(compound_data["fp_shap"], caption="SHAP projection + Morgan bits", use_column_width=True)

elif view_option == "Descriptor SHAP + Kinase Info":
    st.subheader(f"{compound_name} — Descriptor SHAP and Kinase Targets")
    st.image(compound_data["desc_shap"], caption="Descriptor-based SHAP", use_column_width=True)
    st.markdown("### 🧬 Kinase Targets")
    st.code(compound_data["kinase"])
