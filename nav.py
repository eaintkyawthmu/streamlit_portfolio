import streamlit as st

def display_logo(url, width=150):
    """Displays a logo in the sidebar."""
    st.sidebar.subheader("AIML Journal")
    st.sidebar.markdown("Welcome to my AIML Journal 🤖✍️")
    #st.sidebar.image(url, width=width)

    #st.sidebar.image(profile.get('image', ''), width=200, caption='Profile Image', use_column_width=False)  # Display profile image

# Function to load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def custom_navigation(pages):
    """Generates custom navigation in the sidebar."""
    #st.sidebar.subheader("Navigation Menu")
    selection = st.sidebar.radio("Feel free to explore the other pages 😊", list(pages.keys()))
    page = pages[selection]
    page()

    st.sidebar.write("##")
 
    st.sidebar.write("<small>Download My Onepage Resume in docx format...</small>", unsafe_allow_html=True)
    # Resume download button
    with open("/home/eaint/projects/Self/OpenAI_Streamlit/data/resume/eaintkyawthmu_resume2024.docx", "rb") as file: 
        
        btn = st.sidebar.download_button(
            label="Download My Resume",
            data=file,
            file_name="eaintkyawthmu_resume2024.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            key='download-resume'
        )
        