import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title of the app
st.title('Student Engagement Analysis')  # Title updated to reflect new focus

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
                        'previous_scores', 'Internet_Access', 'overall_score']  # Replaced 'performance' with 'overall_score'

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        st.error(f"The following columns are missing from the dataset: {', '.join(missing_columns)}")
    else:
        # Drop rows with missing values in critical columns
        df = df.dropna(subset=required_columns)

        # Visualizing the data
        st.subheader("Visualize Data")

        # Overall Score vs Hours Studied (Scatter Plot)
        st.write("Hours Studied vs Overall Score (Scatter Plot)")
        fig = px.scatter(df, x="hours_studied", y="overall_score", title="Hours Studied vs Overall Score")  # Updated variable
        st.plotly_chart(fig)

        # Overall Score vs Attendance (Box Plot)
        st.write("Overall Score by Attendance (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='attendance', y='overall_score', data=df, ax=ax)  # Updated variable
        ax.set_title('Overall Score Distribution by Attendance')
        st.pyplot(fig)

        # Overall Score by Parental Involvement (Bar Plot)
        st.write("Overall Score by Parental Involvement (Bar Plot)")
        parental_score = df.groupby('parental_involvement')['overall_score'].mean().reset_index()  # Updated variable
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='parental_involvement', y='overall_score', data=parental_score, ax=ax)  # Updated variable
        ax.set_title('Overall Score by Parental Involvement')
        st.pyplot(fig)

        # Overall Score by Access to Resources (Box Plot)
        st.write("Overall Score by Access to Resources (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Access_to_Resources', y='overall_score', data=df, ax=ax)  # Updated variable
        ax.set_title('Overall Score by Access to Resources')
        st.pyplot(fig)

        # Overall Score by Extracurricular Activities (Box Plot)
        st.write("Overall Score by Extracurricular Activities (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Extracurricular_activities', y='overall_score', data=df, ax=ax)  # Updated variable
        ax.set_title('Overall Score by Extracurricular Activities')
        st.pyplot(fig)

        # Previous Scores vs Overall Score (Scatter Plot)
        st.write("Previous Scores vs Overall Score (Scatter Plot)")
        fig = px.scatter(df, x="previous_scores", y="overall_score", title="Previous Scores vs Overall Score")  # Updated variable
        st.plotly_chart(fig)

        # Overall Score by Internet Access (Box Plot)
        st.write("Overall Score by Internet Access (Box Plot)")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x='Internet_Access', y='overall_score', data=df, ax=ax)  # Updated variable
        ax.set_title('Overall Score by Internet Access')
        st.pyplot(fig)

        # Display some specific analysis
        st.subheader("Advanced Analysis")

        # Filter students by overall score
        score_threshold = st.slider("Select Overall Score Threshold", min_value=0, max_value=100, value=50)
        filtered_students = df[df['overall_score'] > score_threshold]  # Updated variable
        st.write(f"Students with overall score greater than {score_threshold}:", filtered_students)

else:
    st.warning("Please upload a CSV file to begin analysis.")


       
        
        
       
        
