import streamlit as st
import pandas as pd

# ===========================
# DATASET SELECTION
# ===========================

st.header("📂 Dataset Selection")

dataset_option = st.radio(
    "Choose Dataset Source",
    (
        "Use Built-in Dataset (Recommended)",
        "Upload Custom Dataset"
    )
)

df = None

if dataset_option == "Use Built-in Dataset (Recommended)":

    dataset_path = "data/callcenter_dataset.json"

    st.success("✅ Built-in dataset selected")

    st.code(dataset_path)

    if st.button("📥 Load Dataset", use_container_width=True):

        with st.spinner("Loading dataset..."):

            df = pd.read_json(dataset_path)

        st.success("Dataset Loaded Successfully!")

else:

    uploaded_file = st.file_uploader(
        "Upload CSV or JSON",
        type=["csv", "json"]
    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_json(uploaded_file)

        st.success("Dataset Uploaded Successfully!")

    if df is not None:

        st.divider()
        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)
        st.divider()
        st.subheader("📊 Dataset Information")



        # streamlit run batch.py --server.maxUploadSize=1024