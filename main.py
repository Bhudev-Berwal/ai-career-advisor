from career_advisor_crew import create_career_advisor_crew

if __name__ == "__main__":
    print("## Welcome to the AI Career & Learning Advisor ##")
    print("------------------------------------------------")
    
    # Get user input from the console
    user_profile = input("Please enter your background, interests, and career goals:\n")
    
    if user_profile:
        # Create and run the crew
        career_advice = create_career_advisor_crew(user_profile)
        
        # Print the results
        print("\n\n########################")
        print("## Here is your personalized career and learning roadmap:")
        print("########################\n")
        print(career_advice)
    else:
        print("No input received. Please run the script again and provide your details.")