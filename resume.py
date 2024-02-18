import streamlit as st
from config import PROFILE, education, experiences

def display_profile(profile):
    col1, col2 = st.columns(2)
    # Add content to the first column
    with col1:
        st.header(profile["name"])
        st.write(profile["contact"])
        st.write(profile["location"])

    # Add content to the second column
    with col2:
        with st.expander("Download resume in .docx ..."):
            st.write("Click the button below to download my onepage resume.")
            # Resume download button
            with open("./data/resume/eaintkyawthmu_resume2024.docx", "rb") as file:
                btn = st.download_button(
                    label="Download My Resume",
                    data=file,
                    file_name="eaintkyawthmu_resume2024.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key='download-my-resume'
                )
        
        st.write(profile["linkedin"])
        st.write(profile["github"])
    st.write("##")

    st.subheader("Summary")
    st.write(profile["summary"])
    st.write("---")

# Education
def display_education(education):
    st.subheader("Education")   
    for edu in education:
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.markdown(f"**{edu['degree']}**")
            st.write(f"{edu['institution']}")
        with col2:
            st.write(f"{edu['year']}")
    st.write("---")

def display_experience(experiences):
    st.subheader("Professional Experiences")
    for exp in experiences:
        with st.expander(f"{exp['title']} at {exp['organization']}"):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.text(f"Location: {exp['location']}")
                for details in exp['details']:
                    st.markdown(f"- {details}")
            with col2:
                st.write(f"{exp['duration']}")
    st.write("---")

# Function to display skills
def display_skills(skills):
    st.subheader("Skills")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Technical Skills**")
        for skill in skills['technical']:
            st.markdown(f"- {skill}")
    
    with col2:
        st.markdown("**Business Skills**")
        for skill in skills['business']:
            st.markdown(f"- {skill}")
        st.markdown("**Soft Skills**")
        for skill in skills['soft']:
            st.markdown(f"- {skill}")

def show():
    display_profile(PROFILE)
    display_education(education)
    display_experience(experiences)
    display_skills(PROFILE['skills'])
