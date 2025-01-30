from dotenv import load_dotenv
import chain
import streamlit as st
import vectordb

# Load environment variables
load_dotenv()

# Initialize the vector store
vectorstore = vectordb.initialize_chroma()

# Set the page config to make the app look better
st.set_page_config(page_title="Brain Tester", layout="wide")

# Apply custom styles for the app (you can add custom CSS here)
st.markdown("""
    <style>
        .css-1d391kg {background-color: #f0f0f5;} /* Adjust sidebar color */
        .css-1lcbmhc {font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;} /* Change font */
        .css-16n5e3f {background-color: #f7f7f7;} /* Main container background color */
        .css-1nbb7jj {background-color: #2e3b4e; color: white;} /* Sidebar heading color */
        .css-15zrgcd {font-size: 18px;} /* Style the title */
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Page", ["Document Ingestion", "Quiz Generator"])

if page == "Document Ingestion":
    st.title("Upload Documents for Testing your Brain 👩‍🏫👨‍🏫")

    # Stylish file uploader with tooltips
    uploaded_file = st.file_uploader(
        "Choose a file (PDF, Word, CSV)", 
        type=["pdf", "docx", "csv"],
        label_visibility="collapsed",  # Hide label to improve UI
        help="Upload your document to test your brain with related content"
    )

    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully! 🎉")
        vectordb.store_pdf_in_chroma(uploaded_file, vectorstore)

else:
    st.title("🧠 Brain Tester Quiz Generator")

    # Custom styling for the quiz section
    st.markdown("""
        <hr style="border-top: 2px solid #2e3b4e;">
        <p style="text-align: center; font-size: 20px; color: #555;">Generate a quiz and test your knowledge!</p>
    """, unsafe_allow_html=True)

    with st.form("Quiz Application"):
        # Number of questions input with enhanced styling and placeholder
        num_questions = st.number_input(
            "Number of questions", min_value=1, max_value=20, value=5,
            help="How many questions would you like in your quiz?"
        )
        
        # Difficulty level input with an easy-to-use dropdown
        difficulty = st.selectbox(
            "Select difficulty level", 
            ["Easy", "Medium", "Hard"],
            help="Choose the difficulty level of the questions."
        )
        
        # Topic input with placeholder and a more detailed tooltip
        topic = st.text_input(
            "Enter topic for the quiz (e.g., Maths, Physics)",
            help="Specify the subject of the quiz (e.g., 'Maths', 'Science')."
        )

        # Checkbox for RAG functionality with additional tooltip
        use_rag = st.checkbox(
            "Use RAG for question generation", 
            help="Enable RAG to generate questions using external context from uploaded documents."
        )

        # Submit button with custom style and hover effect
        submitted = st.form_submit_button("Generate Quiz")

        if submitted:
            if use_rag:
                st.write("Generating questions using RAG... Please wait ⏳")
                response = chain.generate_quiz_rag(num_questions, difficulty, topic, vectorstore)

                # Display questions in a styled way with more interactivity
                if isinstance(response, str):
                    st.write(response)  # If it's a string, just print it
                else:
                    for i, q in enumerate(response, 1):
                        st.write(f"**Question {i}:** {q['question']}")
                        st.radio(f"Choose an option for Question {i}:", q["options"], key=f"question_{i}")

            else:
                st.write("Generating standard quiz questions... Please wait ⏳")
                response = chain.generate_quiz_question(num_questions, difficulty, topic)

                if isinstance(response, str):
                    st.write(response)  # If it's a string, just print it
                else:
                    for i, q in enumerate(response, 1):
                        st.write(f"**Question {i}:** {q['question']}")
                        st.radio(f"Choose an option for Question {i}:", q["options"], key=f"question_{i}")

    # Add footer for a nice touch
    st.markdown("""
        <hr style="border-top: 2px solid #2e3b4e;">
        <p style="text-align: center; color: #888;">Thank you for testing your brain with us! 💡</p>
    """, unsafe_allow_html=True)
