import streamlit as st

st.title("🚀 Git Log Analyzer Dashboard")

uploaded_file = st.file_uploader(
    "Upload Log File",
    type=["log", "txt"]
)

if uploaded_file is not None:
    st.success("File Uploaded Successfully")
    