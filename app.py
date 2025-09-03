import streamlit as st
from career_advisor_crew import create_career_advisor_crew

st.set_page_config(page_title="AI Career Advisor", layout="wide")

# App title and description
st.title("🤖 Multi-Agent AI Career & Learning Advisor")
st.markdown(
    """
    <style>
        .stButton>button {
            width: 100%;
            border-radius: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.write(
    "Struggling to plan your career? Our team of AI agents is here to help! "
    "Describe your background, interests, and goals, and our agents will work together to create a personalized roadmap for you."
)

st.divider()

# User input section
st.header("Tell Us About Yourself")
user_profile = st.text_area(
    "Enter your skills, experience, interests, and career goals here.",
    height=200,
    placeholder="Example: I'm a computer science student interested in data science. I know Python and have a basic understanding of Pandas..."
)

# Button to start the analysis
if st.button("🚀 Get Career Advice"):
    if user_profile:
        # A spinner to show that the process is running
        with st.spinner("Our AI agents are collaborating to build your roadmap... This may take a moment..."):
            try:
                # Kick off the crew with the user's profile
                result = create_career_advisor_crew(user_profile)
                
                st.divider()
                st.header("✨ Your Personalized Career Roadmap")
                # Display the result as markdown for better formatting
                st.markdown(result) 
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.error("Please check your API key and setup, then try again.")
    else:
        st.warning("Please provide your profile information before proceeding.")

# Sidebar for additional information
with st.sidebar:
    st.header("Meet the Agents")
    st.markdown("""
    - **Career Path Advisor**: Suggests potential career tracks.
    - **Skill Gap Analyst**: Identifies missing skills for your desired role.
    - **Learning Advisor**: Recommends courses and resources.
    - **Resume Coach**: Provides tips to tailor your resume.
    """)
    
    st.divider()

    st.header("Tech Stack")
    st.markdown("""
    - **CrewAI**: For multi-agent orchestration.
    - **Streamlit**: For the interactive UI.
    - **Google Gemini**: The language model powering the agents.
    """)