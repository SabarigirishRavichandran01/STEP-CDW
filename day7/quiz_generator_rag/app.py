from dotenv import load_dotenv
import chain
import streamlit as st
load_dotenv()

def quiz_generator_app():
    '''
    Function to generate quiz

    Returns:
        response.content(str)
    '''
    # Set a title for the app with some stylized formatting
    st.markdown("""
    <h1 style="text-align: center; color: #2e3b4e;">Brain Tester Quiz Generator</h1>
    """, unsafe_allow_html=True)

    # Add a description for better user understanding with a friendly tone
    st.markdown("""
    Welcome to the **Brain Tester**! 
    Here you can generate fun and challenging quizzes on any topic. 
    Just choose a topic, the number of questions, and the difficulty level to test your knowledge!
    Let's begin below:
    """)

    # Form for quiz input with a nice card design for better visual appeal
    with st.form("quiz_form", clear_on_submit=True):
        # Topic input with a placeholder and font styling
        topic = st.text_input(
            "Enter the topic to test your brain",
            placeholder="e.g., Science, History, etc.",
            help="Enter the subject for which you want a quiz"
        )
        
        # Number of questions input with a more modern slider design
        num_questions = st.slider(
            "Select number of questions", 
            min_value=1, 
            max_value=100, 
            value=5, 
            step=1,
            help="Choose how many questions you'd like in your quiz."
        )

        # Difficulty level selector with an informative description
        difficulty = st.selectbox(
            "Select the difficulty level", 
            options=["Easy", "Moderate", "Hard"], 
            help="Select the level of challenge you want."
        )

        # Submit button with styling and hover effect
        submitted = st.form_submit_button(label="Generate Quiz")

        # If form is submitted, generate and display the quiz
        if submitted:
            if not topic:
                st.error("Please enter a topic to generate the quiz!")
            else:
                with st.spinner("Generating your quiz..."):
                    response = chain.generate_quiz(topic, num_questions, difficulty)
                    st.success("Quiz Generated Successfully! 🎉")
                    st.info(response)
    
    # Add a separator line to give some space before the footer or closing
    st.markdown("""
    <hr style="border-top: 2px solid #2e3b4e;">
    """, unsafe_allow_html=True)
    st.write("Enjoy your quiz and happy learning! 🧠✨")

    # Add some aesthetic design with markdown for a closing message
    st.markdown("""
    <p style="font-size: 18px; text-align: center; color: #555;">Made with ❤️ by your Brain Tester team!</p>
    """, unsafe_allow_html=True)

# Run the app
quiz_generator_app()
