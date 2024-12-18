import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title of the app
st.title('Student Performance Analysis')

# Sidebar for uploading the data
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data
    df = pd.read_csv(uploaded_file)

    # Display dataset
    st.subheader("Dataset Overview")
    st.write(df.head())

    # Show some basic statistics about the dataset
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Display correlation heatmap
    st.subheader("Correlation Heatmap")
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Visualizing the data
    st.subheader("Visualize Data")

    # Performance vs Study Time plot
    if 'study_time' in df.columns and 'performance' in df.columns:
        st.write("Study Time vs Performance")
        fig = px.scatter(df, x="study_time", y="performance", title="Study Time vs Performance")
        st.plotly_chart(fig)

    # Performance by gender bar chart
    if 'gender' in df.columns and 'performance' in df.columns:
        st.write("Performance by Gender")
        gender_performance = df.groupby('gender')['performance'].mean().reset_index()
        fig, ax = plt.subplots()
        sns.barplot(x='gender', y='performance', data=gender_performance, ax=ax)
        st.pyplot(fig)

    # Performance distribution
    if 'performance' in df.columns:
        st.write("Performance Distribution")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(df['performance'], kde=True, ax=ax)
        st.pyplot(fig)

    # Display some specific analysis
    st.subheader("Advanced Analysis")

    # Filter students by performance
    if 'performance' in df.columns:
        performance_threshold = st.slider("Select Performance Threshold", min_value=0, max_value=100, value=50)
        filtered_students = df[df['performance'] > performance_threshold]
        st.write(f"Students with performance greater than {performance_threshold}:", filtered_students)

else:
    st.warning("Please upload a CSV file to begin analysis.")

       


 