import streamlit as st

# Assuming the projects are defined in a config.py or similar
from config import projects

# Main display function
def show():
    st.title("Projects")
    st.write("Welcome to the projects page! Here's a glimpse of the projects I've been working on.")

    # Display projects in a single column layout
    for project in projects:
        col1, col2, col3 = st.columns([1, 1, 1], gap="large")
        st.markdown("##")
        st.markdown("##")
        with col1:
            st.image(project.get('image', ''), width=300)  # Display image if exists
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                st.markdown(f"**{project['title']}**")
                st.write(project['description'])
            with subcol2:
                st.write(project['duration'])
                if project.get('github_link'):
                    st.button(f'GitHub {project["project_id"]}_col1', on_click=lambda: st.query_params(url=project['github_link']))
            with st.expander("Brief Project Descriptions"):
                for detail in project['details']:
                    st.markdown(f"- {detail}")

        with col2:
            st.image(project.get('image', ''), width=300)  # Display image if exists
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                st.markdown(f"**{project['title']}**")
                st.write(project['description'])
            with subcol2:
                st.write(project['duration'])
                if project.get('github_link'):
                    st.button(f'GitHub {project["project_id"]}_col2', on_click=lambda: st.query_params(url=project['github_link']))
            with st.expander("Brief Project Descriptions"):
                for detail in project['details']:
                    st.markdown(f"- {detail}")

        with col3:
            st.image(project.get('image', ''), width=300)  # Display image if exists
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                st.markdown(f"**{project['title']}**")
                st.write(project['description'])
            with subcol2:
                st.write(project['duration'])
                if project.get('github_link'):
                    st.button(f'GitHub {project["project_id"]}_col3', on_click=lambda: st.query_params(url=project['github_link']))
            with st.expander("Brief Project Descriptions"):
                for detail in project['details']:
                    st.markdown(f"- {detail}")

projects = projects[3:]
# Pagination
if st.button("Next Page"):
    projects = projects[6:]  # Assuming each page displays 6 projects
    show_projects()
