import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Carbon Track",
    page_icon="🌍",
    layout="centered"
)

# --- MAIN APP ---
st.title("🌍 Carbon Track")
st.header("The 'QuickBooks for Carbon' for SMBs")

st.write("This is the live demo for my MSc dissertation project.")
st.write("The goal is to build an end-to-end data platform to automate carbon reporting from unstructured utility bills.")

st.subheader("Project Status:")
st.success("Phase 1: Front-End Deployed (Complete)")
st.info("Phase 2: Back-End API (In Progress)")
st.info("Phase 3: Data Pipeline (Pending)")

st.subheader("Core Technology:")
st.code("""
- Backend API: FastAPI
- Data Pipeline: Apache Airflow
- ML/OCR Model: spaCy + Tesseract
- Database: PostgreSQL
- Frontend: Streamlit
""", language="markdown")

st.markdown("---")
st.write("Find the full project on [GitHub](httpsm://github.com/YOUR-USERNAME/Carbon-Track)") 
# ^^^ IMPORTANT: Change YOUR-USERNAME to your actual GitHub username
