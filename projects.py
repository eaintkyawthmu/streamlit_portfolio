import streamlit as st

# Assuming the projects are defined in a config.py or similar
from config import projects

# Main display function
def show():
    st.title("Projects")
    st.write("Welcome to the projects page! Here's a glimpse of the projects I've been working on.")
    
    for project in projects:
        col1, col2 = st.columns([1, 1], gap="large")
        with col1:
            if project.get('image'):  # Check if the image exists before displaying
                st.image(project.get('image'), width=350)
        with col2:
            st.markdown(f"#### {project['title']}")
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                st.write(project['description'])
                # if project.get('demo_link'):
                #     # Use markdown to create a clickable link instead of a button
                #     demo_link = project['demo_link']
                #     demo_text = f"[Demo]({demo_link})"
                #     st.markdown(f"#### {demo_text}")
                    
                if project.get('github_link'):
                    # Use markdown to create a clickable link instead of a button
                    github_link = project['github_link']
                    link_text = f"[GitHub]({github_link})"
                    st.markdown(f"#### {link_text}")

            with subcol2:
                st.write(project['duration'])
                st.markdown("##")

        with st.expander("Brief Project Descriptions"):

            for detail in project['details']:
                st.markdown(f"- {detail}")
        st.markdown("##")
