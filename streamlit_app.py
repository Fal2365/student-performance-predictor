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

    # Visualizing the data
    st.subheader("Visualize Data")

    # Performance vs Study Time scatter plot
    st.write("Study Time vs Performance")
    fig = px.scatter(df, x="study_time", y="performance", title="Study Time vs Performance")
    st.plotly_chart(fig)

    # Box plot of performance distribution by gender
    st.write("Performance by Gender (Box Plot)")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='gender', y='performance', data=df, ax=ax)
    ax.set_title('Performance Distribution by Gender')
    st.pyplot(fig)

    # Performance trend over study time (Line plot)
    st.write("Performance Trend by Study Time (Line Plot)")
    performance_trend = df.groupby('study_time')['performance'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='study_time', y='performance', data=performance_trend, ax=ax)
    ax.set_title('Performance Trend by Study Time')
    st.pyplot(fig)

    # Display some specific analysis
    st.subheader("Advanced Analysis")

    # Filter students by performance
    performance_threshold = st.slider("Select Performance Threshold", min_value=0, max_value=100, value=50)
    filtered_students = df[df['performance'] > performance_threshold]
    st.write(f"Students with performance greater than {performance_threshold}:", filtered_students)

    # Additional analysis could be added here based on the data, such as clustering, regression models, etc.

else:
    st.warning("Please upload a CSV file to begin analysis.")

    

   


 
