# 🤖 Multi-Agent AI Career & Learning Advisor

This project is an AI-powered Career & Learning Advisor where a team of specialized AI agents collaborates to provide personalized career guidance, identify skill gaps, recommend learning resources, and offer resume advice. It's built using CrewAI, Streamlit, and Google Gemini.



## 🎯 Problem Statement

Students and professionals often struggle with planning their careers. Choosing the right skills to learn, finding relevant courses, and tailoring a resume for a specific job can be overwhelming. This project uses a multi-agent system to mimic a team of real-world mentors: a career coach, a skills analyst, a learning specialist, and a resume expert all working together for the user.

## ✨ Features

-   **Multi-Agent Collaboration**: Four specialized AI agents work in sequence to build a comprehensive career plan.
-   **Personalized Advice**: Guidance is tailored to the user's unique background, interests, and goals.
-   **End-to-End Roadmap**: Provides a complete plan from career path selection to resume improvement.
-   **Interactive UI**: A simple and clean user interface built with Streamlit.

## 🛠️ Tech Stack

-   **Framework**: [CrewAI](https://www.crewai.com/) for orchestrating the multi-agent system.
-   **UI**: [Streamlit](https://streamlit.io/) for the interactive web application.
-   **Language Model (LLM)**: Powered by Google Gemini.
-   **Language**: Python

## 🧠 The Agents

1.  **Career Path Agent**: Suggests possible career tracks based on the user's profile.
2.  **Skill Gap Agent**: Analyzes a chosen career path to identify missing skills.
3.  **Learning Advisor Agent**: Recommends online courses and projects to bridge skill gaps.
4.  **Resume Coach Agent**: Reviews the user's profile and suggests resume improvements.

## ⚙️ Setup and Installation

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone [https://github.com/Bhudev-Berwal/ai-career-advisor.git](https://github.com/Bhudev-Berwal/ai-career-advisor.git)
cd ai-career-advisor
```

### 2. Create a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

-   Create a file named `.env` in the root directory.
-   Add your Google Gemini API key to this file. You can get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey).

```text
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

### 5. Run the Application

```bash
streamlit run app.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).