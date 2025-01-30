from model import create_chat_groq_model
import prompt
import vectordb    

def generate_quiz_question(num_questions, difficulty, topic):
    """
    Function to generate multiple quiz questions.
    """
    prompt_template = prompt.quiz_generator_prompt()
    llm = create_chat_groq_model()

    chain = prompt_template | llm

    response = chain.invoke({
        "num_questions": num_questions,
        "difficulty": difficulty,
        "topic": topic
    })

    print("Raw LLM Response:", response.content)

    return extract_text_content(response.content)  # Use the extraction function for text output

def generate_quiz_rag(num_questions, difficulty, topic, vectorstore):
    """
    Function to generate quiz questions using RAG (Retrieval-Augmented Generation).
    """
    prompt_template = prompt.quiz_generator_rag_prompt()
    llm = create_chat_groq_model()

    retrieved_docs = vectordb.retrieve_from_chroma(topic, vectorstore)  # <-- Pass vectorstore
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    chain = prompt_template | llm

    response = chain.invoke({
        "num_questions": num_questions,
        "difficulty": difficulty,
        "topic": topic,
        "context": context
    })

    print("Raw LLM Response:", response.content)

    return extract_text_content(response.content)  # Use the extraction function for text output

def extract_text_content(response_text):
    """
    Extracts the relevant text content from the LLM response and returns it as a string.
    """
    print("Raw response:", response_text)  # Debugging print

    try:
        return response_text.strip() 
    except Exception as e:
        print("Error while extracting text content:", e)
        return "Error: Failed to extract text content."
