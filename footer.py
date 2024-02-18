import streamlit as st
# Function to load HTML
def load_html(file_name):        
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def custom_footer():
    st.write("---")
    st.markdown('<style>.footer {position:relative; bottom: 0; width: auto; text-align: center; margin-left: -5px; margin-right: -5px; padding: 3px; list-style: none; display: flex; justify-content: center; margin-top: 0px;}</style>', unsafe_allow_html=True)
    st.markdown('<div class="footer"> Whether it is a question, inquiries or just a hello, you can find me on the social platforms below. </div>', unsafe_allow_html=True)
    st.write('<div class="footer">Thank you for visiting!</div>', unsafe_allow_html=True)

    # Load and display social links
    social_links_html = load_html("/home/eaint/projects/Self/OpenAI_Streamlit/data/html/social_links.html")
    st.markdown(social_links_html, unsafe_allow_html=True)

    st.markdown('<div class="footer">© 2021 AIML Journal. All rights reserved.</div>', unsafe_allow_html=True)