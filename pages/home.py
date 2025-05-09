import streamlit as st
from datetime import datetime

def home_page():
    st.title("👩‍💻 AI Career & Community Assistant")
    st.markdown("### Empower Your Career Journey with AI ✨")

    st.markdown("""
    Welcome to the **AI Career & Community Assistant**, your personalized platform to:
    - 🔍 Discover jobs
    - 📄 Analyze your resume
    - 💬 Get real-time career advice
    - 📅 Stay updated with tech events

    This tool is designed to help students, professionals, and job seekers make informed decisions and level up their career with the power of **AI-driven insights**.
    """)

    st.markdown("---")
    st.subheader("🛠 Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💬 **Community Assistant**\nAsk career questions, get resume tips, interview prep help & more.")

    with col2:
        st.success("🔍 **Job Search**\nFind relevant job openings tailored to your field and skills.")

    with col3:
        st.warning("📄 **Resume Analyzer**\nUpload your resume and get improvement suggestions instantly.")

    col4, _ = st.columns([1, 2])
    with col4:
        st.image("https://via.placeholder.com/150", caption="AI-Powered Career Assistant")
    st.markdown("---")

    st.subheader("🚀 Why Use This App?")
    st.markdown("""
    - ✅ Centralized platform for career tools  
    - ✅ AI-powered assistance and automation  
    - ✅ Simple and user-friendly UI  
    - ✅ Constantly improving and expanding  

    Whether you're a **fresh graduate**, **career switcher**, or **seasoned pro**, this app is your companion to smarter job search and growth.
    """)

    st.markdown("---")

    st.info(f"🕒 Today's Date: {datetime.now().strftime('%A, %d %B %Y')}")
    st.caption("Version 1.0 • Made with ❤️ using Streamlit")
