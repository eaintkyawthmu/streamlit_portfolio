import streamlit as st
import requests

def show():

    st.subheader("Blog Posts")   
    # Sanity API endpoint
    url = "https://ugsaokcj.api.sanity.io/v2022-03-07/data/query/production?query=*[_type == 'post']{title, author->{name}}"

    # Fetch data
    response = requests.get(url)
    posts = response.json()['result']

    # Display posts
    with st.markdown("Recent Posts"):
        for post in posts:
            st.write(f"### {post['title']}")
            st.write(f"**Author:** {post['author']['name']}")