import streamlit as st
import pandas as pd

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="HBR-Uber Case Study Dashboard", layout="wide")

# ---------------------------
# Header With Two Logos
# ---------------------------
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.image("left_logo.png", width=90)   # Replace with your left logo file

with col2:
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 36px;'>
            HBR – Uber – Case Study Dashboard
        </h1>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.image("right_logo.png", width=90)  # Replace with your right logo file

st.markdown("---")

# ---------------------------
# Create Tabs
# ---------------------------
tab1, tab2, tab3 = st.tabs(["📁 METs Data", "📘 Data Dictionary", "📊 Visualizations"])

# ----------------------------------------
# TAB 1 – METs DATA
# ----------------------------------------
with tab1:
    st.header("📁 METs Data")
    
    uploaded_file = st.file_uploader("Upload METs CSV File", type=["csv"])

    if uploaded_file:
        mets_df = pd.read_csv(uploaded_file)
        st.write("### METs Data Preview")
        st.dataframe(mets_df, use_container_width=True)
    else:
        st.info("Upload a METs dataset to view it here.")


# ----------------------------------------
# TAB 2 – DATA DICTIONARY
# ----------------------------------------
with tab2:
    st.header("📘 Data Dictionary")

    uploaded_dict = st.file_uploader("Upload Data Dictionary CSV", type=["csv"], key="dict")

    if uploaded_dict:
        dict_df = pd.read_csv(uploaded_dict)
        st.write("### Data Dictionary Preview")
        st.dataframe(dict_df, use_container_width=True)
    else:
        st.info("Upload a Data Dictionary file to view it here.")


# ----------------------------------------
# TAB 3 – VISUALIZATIONS
# ----------------------------------------
with tab3:
    st.header("📊 Visualizations")

    uploaded_viz = st.file_uploader("Upload dataset for visualization", type=["csv"], key="viz")

    if uploaded_viz:
        viz_df = pd.read_csv(uploaded_viz)

        st.write("### Dataset Preview")
        st.dataframe(viz_df, use_container_width=True)

        # Basic Visualizations (Examples)
        st.write("### Column Selection")
        numeric_cols = viz_df.select_dtypes(include=["float64", "int64"]).columns

        if len(numeric_cols) >= 2:
            x_col = st.selectbox("Select X-axis", numeric_cols)
            y_col = st.selectbox("Select Y-axis", numeric_cols)

            st.line_chart(viz_df[[x_col, y_col]])
        else:
            st.warning("Not enough numeric columns to visualize.")

    else:
        st.info("Upload a dataset to generate visualizations.")

