import streamlit as st
import nav , footer
from home import show as home_show
from resume import show as resume_show
from blog import show as blog_posts_show
from projects import show as projects_show

# Set page configuration
st.set_page_config(
    page_title="AIML Journal",
    page_icon=":computer:",
    layout="centered",
    initial_sidebar_state="expanded"
)
# Function to load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    local_css("style.css")  # Load CSS

    
def main():
    # Display the logo at the top of the sidebar
   # nav.display_logo("/home/eaint/projects/Self/OpenAI_Streamlit/data/images/avatar.jpg")
    #https://picsum.photos/536/354

    # Define your pages
    
    pages = {
        "Home": home_show,
        "Resume": resume_show,
        # "Projects": projects_show,
        "Blog Posts": blog_posts_show,        
    }

    # Set up custom navigation
    nav.custom_navigation(pages)
    footer.custom_footer()

if __name__ == "__main__":
    main()