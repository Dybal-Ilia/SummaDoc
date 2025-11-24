import streamlit as st
import requests

st.title("📄 Document Summarizer")

uploaded_file = st.file_uploader(
    "Upload a document", type=["pdf", "docx", "txt", "md"]
)

if uploaded_file is not None:
    with st.spinner("Generating summary..."):
        response = requests.post(
            "http://127.0.0.1:8000/summarize/",
            files={"file": uploaded_file}
        )
        if response.status_code == 200:
            data = response.json()
            st.subheader("Summary:")
            st.write(data["summary"])
        else:
            st.error("Failed to summarize the document.")
