import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# 1. Career Path Agent
career_path_agent = Agent(
    role="Career Path Advisor",
    goal="Suggest 3-5 potential career tracks based on the user's background, interests, and goals. Provide a brief description for each.",
    backstory=(
        "You are an experienced career coach who specializes in the tech industry. "
        "You have a deep understanding of various roles, from software engineering to data science and product management. "
        "Your goal is to help users discover career paths that align with their passions and skills."
    ),
    verbose=True,
    llm=llm,
    allow_delegation=False,
)

# 2. Skill Gap Agent
skill_gap_agent = Agent(
    role="Skill Gap Analyst",
    goal="Analyze a chosen career path and identify the key skills, tools, and technologies required. Compare these with the user's current skills to find any gaps.",
    backstory=(
        "You are a meticulous analyst with a knack for breaking down job descriptions into core competencies. "
        "You stay up-to-date with the latest industry trends and know exactly what skills are in demand for any given tech role. "
        "Your analysis is data-driven and precise."
    ),
    verbose=True,
    llm=llm,
    allow_delegation=True,
)

# 3. Learning Advisor Agent
learning_advisor_agent = Agent(
    role="Learning and Development Specialist",
    goal="Recommend specific online courses, tutorials, books, and projects to help the user bridge their skill gaps. Provide links and brief descriptions.",
    backstory=(
        "You are a passionate educator and content curator who loves helping people learn. "
        "You have a vast knowledge of online learning platforms like Coursera, Udemy, freeCodeCamp, and can find the best resources for any topic. "
        "You focus on practical, high-quality recommendations."
    ),
    verbose=True,
    llm=llm,
    allow_delegation=False,
)

# 4. Resume Coach Agent
resume_coach_agent = Agent(
    role="Resume Optimization Coach",
    goal="Review the user's profile or resume summary and provide actionable advice to tailor it for a specific job or career path. Suggest improvements to highlight relevant skills and experiences.",
    backstory=(
        "You are a former tech recruiter and professional resume writer. "
        "You know what hiring managers look for and how to make a resume stand out. "
        "Your advice is practical, direct, and aimed at getting interviews."
    ),
    verbose=True,
    llm=llm,
    allow_delegation=False,
)

# Define Tasks
# Task for Career Path Agent
career_path_task = Task(
    description=(
        "Based on the user's input: {user_profile}, identify and suggest 3 to 5 promising career paths. "
        "For each path, provide a concise one-paragraph description explaining the role and why it's a good fit."
    ),
    expected_output="A formatted report with 3-5 career path suggestions, each with a title and a brief description.",
    agent=career_path_agent,
)

# Task for Skill Gap Agent
skill_gap_task = Task(
    description=(
        "Analyze the career paths suggested by the Career Path Advisor. For each path, list the essential technical and soft skills required. "
        "Then, compare these requirements with the user's current skills from their profile: {user_profile}. "
        "Clearly identify the missing skills (the 'skill gap')."
    ),
    expected_output="A detailed analysis for each career path, listing required skills and explicitly highlighting the user's skill gaps.",
    agent=skill_gap_agent,
    context=[career_path_task] # This task depends on the output of the career_path_task
)

# Task for Learning Advisor Agent
learning_advisor_task = Task(
    description=(
        "Based on the identified skill gaps, recommend a list of high-quality learning resources. "
        "For each skill gap, suggest at least two resources (e.g., a specific Coursera course, a YouTube tutorial series, a book, or a hands-on project idea). "
        "Provide direct links where possible."
    ),
    expected_output="A curated list of learning resources, organized by skill, with links and brief explanations on why each resource is valuable.",
    agent=learning_advisor_agent,
    context=[skill_gap_task]
)

# Task for Resume Coach Agent
resume_coach_task = Task(
    description=(
        "Review the user's profile: {user_profile} and the suggested career paths. "
        "Provide 3-5 concrete, actionable tips to improve their resume or professional summary. "
        "The advice should be tailored to help them land a job in the recommended fields. "
        "Focus on phrasing, project descriptions, and skill highlighting."
    ),
    expected_output="A bullet-point list of 3-5 actionable resume improvement suggestions, tailored to the recommended career paths.",
    agent=resume_coach_agent,
    context=[career_path_task, skill_gap_task]
)

# Define the function to create and run the crew
def create_career_advisor_crew(user_profile):
    """Creates and kicks off the career advisor crew."""
    career_crew = Crew(
        agents=[career_path_agent, skill_gap_agent, learning_advisor_agent, resume_coach_agent],
        tasks=[career_path_task, skill_gap_task, learning_advisor_task, resume_coach_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        verbose=2
    )
    
    result = career_crew.kickoff(inputs={'user_profile': user_profile})
    return result