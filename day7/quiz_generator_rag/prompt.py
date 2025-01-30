from langchain_core.prompts import ChatPromptTemplate

def quiz_generator_prompt():
    """
    Generates a prompt template for quiz generation.
    """
    system_msg = """
        You are a quiz generator assistant. Generate multiple-choice questions based on the given topic and difficulty.

        Provide the questions and options as a simple text output:
        Question: What is AI?
        Options: ML, DL, NN, AI
        Correct Answer: AI
    """

    user_msg = "Generate {num_questions} {difficulty}-level quiz questions on the topic: {topic}."

    return ChatPromptTemplate.from_messages([("system", system_msg), ("user", user_msg)])

def quiz_generator_rag_prompt():
    """
    Generates a RAG-based prompt template for quiz generation.
    """
    system_msg = """
        You are a quiz generator assistant that retrieves relevant information before generating quiz questions.

        Provide the questions and options as a simple text output:
        Question: What is AI?
        Options: ML, DL, NN, AI
        Correct Answer: AI
    """

    user_msg = "Generate {num_questions} {difficulty}-level quiz questions on {topic} using this document:\n{context}"

    return ChatPromptTemplate.from_messages([("system", system_msg), ("user", user_msg)])