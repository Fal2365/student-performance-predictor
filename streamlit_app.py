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

    # Check required columns
    required_columns = ['Hours_Studied', 'Exam_Score', 'Gender']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        st.error(f"The following columns are missing from the dataset: {', '.join(missing_columns)}")
    else:
        # Display dataset
        st.subheader("Dataset Overview")
        st.write(df.head())

        # Show some basic statistics about the dataset
        st.subheader("Basic Statistics")
        st.write(df.describe())

        # Visualizing the data
        st.subheader("Visualize Data")

        # Performance vs Study Time scatter plot
        st.write("Hours Studied vs Exam Score")
        fig = px.scatter(df, x="Hours_Studied", y="Exam_Score", title="Hours Studied vs Exam Score")
        st.plotly_chart(fig)

        # Box plot of performance distribution by gender
        st.write("Exam Score by Gender (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Gender', y='Exam_Score', data=df, ax=ax)
        ax.set_title('Exam Score Distribution by Gender')
        st.pyplot(fig)

        # Performance trend over study time (Line plot)
        st.write("Exam Score Trend by Hours Studied (Line Plot)")
        performance_trend = df.groupby('Hours_Studied')['Exam_Score'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.lineplot(x='Hours_Studied', y='Exam_Score', data=performance_trend, ax=ax)
        ax.set_title('Exam Score Trend by Hours Studied')
        st.pyplot(fig)

        # Display some specific analysis
        st.subheader("Advanced Analysis")

        # Filter students by performance
        performance_threshold = st.slider("Select Exam Score Threshold", min_value=0, max_value=100, value=50)
        filtered_students = df[df['Exam_Score'] > performance_threshold]
        st.write(f"Students with Exam Score greater than {performance_threshold}:", filtered_students)

        # Additional analysis could be added here based on the data, such as clustering, regression models, etc.

else:
    st.warning("Please upload a CSV file to begin analysis.")

    
        
       

       
        
        
       
        
