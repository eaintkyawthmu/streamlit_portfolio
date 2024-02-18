import streamlit as st
from config import PROFILE, education, experiences, projects
from projects import show as projects_show
from streamlit_option_menu import option_menu
import requests
import json

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_profile():
    
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        st.markdown('<h5>Hi, I\'m Eaint <img src="https://raw.githubusercontent.com/nixin72/nixin72/master/wave.gif" alt="Waving hand animated gif" height="40" width="40" /></h5>', unsafe_allow_html=True)
        st.write(PROFILE["aboutme"])
        in_col1, in_col2 , in_col3 = st.columns([0.1, 0.8, 0.1])
        with in_col1:
            st.write("##")
        with in_col2:
            st.markdown('<blockquote> My journey in data science is a journey of discovery, a journey of transformation, and a journey of impact.</blockquote>', unsafe_allow_html=True)

            # Load and display social links
            # Function to load HTML
            def load_html(file_name):        
                with open(file_name, 'r', encoding='utf-8') as file:
                    return file.read()
            social_links_html = load_html("./data/html/social_links.html")
            st.markdown(social_links_html, unsafe_allow_html=True)
        with in_col3:
            #st.image("https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png", width=200, caption='photos by Sherlock Project', use_column_width=False)  # Display profile image
            st.write("##")

    with col2:
        st.write("##")
        st.image(PROFILE.get('image', ''), width=200, use_column_width=False)
    
    st.write("---")

   
# BlogPosts
def display_sanityposts():
    st.subheader("Blog Posts")   
    # Sanity API endpoint
    url = "https://ugsaokcj.api.sanity.io/v2022-03-07/data/query/production?query=*[_type == 'post']{title, author->{name}}"

    # Fetch data
    response = requests.get(url)
    posts = response.json()['result']

    # Display posts
    with st.expander("Recent Posts"):
        for post in posts:
            st.write(f"### {post['title']}")
            st.write(f"**Author:** {post['author']['name']}")

# def display_experience(experiences):
#     st.subheader("Professional Experiences")
#     for exp in experiences:
#         with st.expander(f"{exp['title']} at {exp['organization']}"):
#             col1, col2 = st.columns([0.8, 0.2])
#             with col1:
#                 st.text(f"Location: {exp['location']}")
#                 for details in exp['details']:
#                     st.markdown(f"- {details}")
#             with col2:
#                 st.write(f"{exp['duration']}")
#     st.write("---")

# def display_projects(projects):
#     for project in projects:
#         st.write(f"## {project['title']}")
#         st.write(project['description'])
#         st.write(f"GitHub: [{project['title']}]({project['github_link']})")
#         st.write(f"Demo: [{project['title']}]({project['demo_link']})")
#     st.write("---")

def show():
    local_css("style.css")  # Load CSS
    display_profile()
    projects_show()
    # display_sanityposts()


# def misc():
       
#     with st.expander("Book details"):
#         st.write("Something about the book")

#     with st.expander("How to buy?"):
#         st.write("How to buy the book")

    # Add a footer to the page
