import streamlit as st
from streamlit_option_menu import option_menu

# Function to load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def show():
    # Load CSS
    local_css("style.css")  # Load CSS

    # Create a container to organize content using Streamlit's container feature
    st.markdown("<h3 style='text-align: center;'> My Journey of Discovery ... </h3>", unsafe_allow_html=True)
    st.markdown("#")
    
    # 2. horizontal menu

    pagecol1 , pagecol2, pagecol3 = st.columns([0.3, 0.4, 0.3])
    with pagecol1:
        
        chapter_selected = option_menu(None, [" US Chapter ", " Australia Chapter ", " Myanmar Chapter "], 
                                    
            icons=['🇺🇸', '🇦🇺', '🇲🇲'], 
            menu_icon="cast", default_index=0, orientation="horizontal",
            styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "nav-link-selected": {"background-color": "#96502a"},
                }
        )
        if chapter_selected == " US Chapter ":
            st.markdown("#")
            st.markdown("##### Milestones Achieved in the United States ##### ")
            st.markdown("#")
            with st.container(): #left
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander('###### ML Project : Analysis of Gene Expression Data for Cancer Classification ######', expanded=False):
                        st.markdown("Participated in AI/ML Capstone Project at Caltech CTME, focusing on ICMR Cancer Genes Analysis utilizing advanced data analysis technologies")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.markdown('<small> Feb 2024 </small>', unsafe_allow_html=True)                       
        
            #-----------------------------------------------------#                    
            with st.container(): #right
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small") 
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.markdown('<small> Mar 2023 <br> ~ <br> Feb 2024 </small>', unsafe_allow_html=True)                       
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                with st.expander("###### Completed Postgraduate Certificate in AI and Machine Learning at Caltech", expanded=False):
                        st.markdown("""Gained a comprehensive overview of various machine learning concepts and their practical applications at the Caltech Center for Technology and Management Education, USA.""")

            
            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### Tech-Driven Entrepreneur & Data Engineer Managing Owner at YoeYoeLay LLC, International Logistics", expanded=False):
                        st.markdown("""
                        Spearheaded YoeYoeLay LLC, enhancing international cargo shipping and e-commerce operations between the US and Myanmar through innovative data science and ML solutions. Leveraged cloud technologies to optimize service delivery.
                                    Implemented data science and ML solutions at YoeYoeLay LLC, focusing on leveraging cloud technologies to enhance e-commerce and international logistics, effectively bridging US-Myanmar markets
                        """)
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.markdown('<small> Sep 2022 </small>', unsafe_allow_html=True)                       
                with main_col3:
                        st.write("##")
            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.write("#")
                        st.markdown('<small> Oct 2023 </small>', unsafe_allow_html=True)                                
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander('###### Fundamentals of Visualization with Tableau University of California, Davis ######', expanded=False):
                        st.markdown("  Fundamentals of Visualization with Tableau University of California, Davis ")
    
            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### Google Certificate", expanded=False):
                        st.markdown("""
                        Attract and Engage Customers with Digital Marketing
                        """)
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.markdown('<small> Jan 2023 </small>', unsafe_allow_html=True)                        
                with main_col3:
                        st.write("##")
            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.write("#")
                        st.markdown('<small> Jan 2023 </small>', unsafe_allow_html=True)            
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander('###### Google Foundations of Digital Marketing and E-commerce ######', expanded=False):
                        st.markdown("Foundations of Digital Marketing and E-commercenma")

        if chapter_selected == " Australia Chapter ":
            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### AS in Business Administration and Management, Canberra Institute of Technology,", expanded=False):
                        st.markdown("""
                        Gained foundational knowledge in business administration, supplemented by technical skills in SQL, Data Collection, and Microsoft Office, contributing to my versatility in business and technology.
                        """)
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.markdown('<small>  Feb 2017 <br> ~ <br> Aug 2018 </small>', unsafe_allow_html=True)                        
                with main_col3:
                        st.write("##")
            
            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.markdown('<small>  Feb 2017 <br> ~ <br> Aug 2018   </small>', unsafe_allow_html=True)            
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander('###### Silo Bakery ######', expanded=False):
                        st.markdown("Bakery Assistant")

            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### Professional Certified Coach of NLP - The ABNLP, Issued", expanded=False):
                        st.markdown("""
                        Achieved certification as a Professional Certified Coach of Neuro-Linguistic Programming (NLP), enhancing communication, personal development, and coaching skills.
                        """)

                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.markdown('<small> Nov 2017 </small>', unsafe_allow_html=True)                        
                with main_col3:
                        st.write("##")
            
            with st.container():
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.markdown('<small>  Feb 2017 <br> ~ <br> Aug 2018   </small>', unsafe_allow_html=True)            
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander('###### Itilian Diner ######', expanded=False):
                        st.markdown("Restaurant Assistant")

        if chapter_selected == " Myanmar Chapter ":
            st.markdown("#")
            st.write("##### Key Milestones Established in Myanmar #####")
            st.markdown("#")
            
            with st.container(): #left
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander('###### External Product Launch Coordinator ,', expanded=False):
                        st.markdown("2C2P · Contract")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.markdown('<small> Feb 2020  <br> ~ <br> Mar 2020 </small>', unsafe_allow_html=True)
                with main_col3:
                        st.write("##")
            with st.container(): #right
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.markdown('<small> Jun 2019 <br> ~ <br> Nov 2019 </small>', unsafe_allow_html=True)          
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                with st.expander("###### Marketing Communication Consultant I'mStylist ", expanded=False):
                        st.markdown("""Gained a comprehensive overview of various machine learning concepts and their practical applications at the Caltech Center for Technology and Management Education, USA.""")

            with st.container(): #left
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### Digital Marketing ConsultantDigital Marketing Consultant AAT Business Park ", expanded=False):
                        st.markdown("""
                        Directed digital marketing strategies for over 34 brands, integrating advanced data analytics to drive growth and enhance online presence. Focused on scalable, data-driven approaches to marketing in the digital age.
                        """)
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.markdown('<small> Sep 2018  <br> ~ <br> Jun 2021 </small>', unsafe_allow_html=True)
                with main_col3:
                        st.write("##")
            with st.container(): #right
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("#")
                        st.markdown('<small> 2018 </small>', unsafe_allow_html=True)          
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander("###### Diploma in E-Business Alison ", expanded=False):
                        st.markdown("""
                        Diploma in E-Business Alison """)

            with st.container(): #left
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### Founder of iDEAHUB Digital Marketing", expanded=False):
                        st.markdown("""
                        Directed digital marketing strategies for over 34 brands, integrating advanced data analytics to drive growth and enhance online presence. Focused on scalable, data-driven approaches to marketing in the digital age.
                        """)
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.markdown('<small> Sep 2018  <br> ~ <br> Jun 2021 </small>', unsafe_allow_html=True)
                with main_col3:
                        st.write("##")
            with st.container(): #right
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.markdown('<small> Jun 2016 <br> ~ <br> Dec 2016 </small>', unsafe_allow_html=True)          
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander("###### AAA", expanded=False):
                        st.markdown("""
                        Focused on marketing principles and data analytics, istrategies. """)

            with st.container(): #left
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### SIYB Licensed Trainer ILO", expanded=False):
                        st.markdown("""
                        Directed digital marketing strategies for over 34 brands, integrating advanced data analytics to drive growth and enhance online presence. Focused on scalable, data-driven approaches to marketing in the digital age.
                        """)
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.markdown('<small> Jun 2015 </small>', unsafe_allow_html=True)
                with main_col3:
                        st.write("##")

            with st.container(): #right
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.markdown('<small> Jun 2016  <br> ~ <br> Dec 2016 </small>', unsafe_allow_html=True)          
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander("###### Marketing Management, Strategy First University - SFU, Jun 2016 - Dec 2016", expanded=False):
                        st.markdown("""
                        Focused on marketing principles and data analytics, including practical applications like A/B testing to drive marketing strategies. """)

            with st.container(): #left
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander('###### Co-Founder MPPG - Mobile Phone Professional Group', expanded=False):
                        st.markdown("MPPG")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("#")
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.markdown('<small> Jan 2014 <br> ~ <br> Feb 2018  </small>', unsafe_allow_html=True)
                with main_col3:
                        st.write("##")
            with st.container(): #right
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.markdown('<small> Nov 2011 <br> ~ <br> Jun 2013 </small>', unsafe_allow_html=True)          
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                with st.expander("###### Net3 Internet Cafe", expanded=False):
                        st.markdown("""Gained a comprehensive overview of various machine learning concepts and their practical applications at the Caltech Center for Technology and Management Education, USA.""")
            with st.container(): #left
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                    with st.expander("###### BA in English Language and Literature, University of Foreign Languages (Mandalay), 2008 - 2011", expanded=False):
                        st.markdown("""
                        Specialized in English Language and Literature, gaining comprehensive skills in communication, analysis, and critical thinking.
                        """)
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2], gap="small")
                    with col1:
                        st.write("---")
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.markdown('<small> Jun 2008 <br> ~ <br> Dec 2011 </small>', unsafe_allow_html=True)
                with main_col3:
                        st.write("##")
            with st.container(): #right
                main_col1, main_col2, main_col3 = st.columns([0.3, 0.4, 0.3], gap="small")
                with main_col1:
                        st.write("##")
                with main_col2:
                    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
                    with col1:
                        st.markdown('<small> Jun 2008 <br> ~ <br> Apr 2010 </small>', unsafe_allow_html=True)          
                    with col2:
                        st.image("https://picsum.photos/200/200", caption="")
                    with col3:
                        st.write("#")
                        st.write("---")
                with main_col3:
                    with st.expander("###### Achieved Diploma in Information Technology, National Centre for Human Resource Development", expanded=False):
                        st.markdown("""
                        Acquired a solid foundation in IT, focusing on SQL, Microsoft Office, and HTML, laying the groundwork for future technological advancements.
                        """)


                        