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

    # Check if necessary columns exist
    required_columns = ['hours_studied', 'attendance', 'parental_involvement', 
                        'Access_to_Resources', 'Extracurricular_activities', 
                        'previous_scores', 'Internet_Access', 'performance']

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        st.error(f"The following columns are missing from the dataset: {', '.join(missing_columns)}")
    else:
        # Drop rows with missing values in critical columns
        df = df.dropna(subset=required_columns)

        # Visualizing the data
        st.subheader("Visualize Data")

        # Performance vs Hours Studied (Scatter Plot)
        st.write("Hours Studied vs Performance (Scatter Plot)")
        fig = px.scatter(df, x="hours_studied", y="performance", title="Hours Studied vs Performance")
        st.plotly_chart(fig)

        # Performance vs Attendance (Box Plot)
        st.write("Performance by Attendance (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='attendance', y='performance', data=df, ax=ax)
        ax.set_title('Performance Distribution by Attendance')
        st.pyplot(fig)

        # Performance by Parental Involvement (Bar Plot)
        st.write("Performance by Parental Involvement (Bar Plot)")
        parental_performance = df.groupby('parental_involvement')['performance'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='parental_involvement', y='performance', data=parental_performance, ax=ax)
        ax.set_title('Performance by Parental Involvement')
        st.pyplot(fig)

        # Performance by Access to Resources (Box Plot)
        st.write("Performance by Access to Resources (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Access_to_Resources', y='performance', data=df, ax=ax)
        ax.set_title('Performance by Access to Resources')
        st.pyplot(fig)

        # Performance by Extracurricular Activities (Box Plot)
        st.write("Performance by Extracurricular Activities (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Extracurricular_activities', y='performance', data=df, ax=ax)
        ax.set_title('Performance by Extracurricular Activities')
        st.pyplot(fig)

        # Previous Scores vs Performance (Scatter Plot)
        st.write("Previous Scores vs Performance (Scatter Plot)")
        fig = px.scatter(df, x="previous_scores", y="performance", title="Previous Scores vs Performance")
        st.plotly_chart(fig)

        # Performance by Internet Access (Box Plot)
        st.write("Performance by Internet Access (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Internet_Access', y='performance', data=df, ax=ax)
        ax.set_title('Performance by Internet Access')
        st.pyplot(fig)

        # Display some specific analysis
        st.subheader("Advanced Analysis")

        # Filter students by performance
        performance_threshold = st.slider("Select Performance Threshold", min_value=0, max_value=100, value=50)
        filtered_students = df[df['performance'] > performance_threshold]
        st.write(f"Students with performance greater than {performance_threshold}:", filtered_students)

else:
    st.warning("Please upload a CSV file to begin analysis.")
