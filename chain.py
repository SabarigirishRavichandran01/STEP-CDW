from model import create_chatgroq
import prompt

def generate_quiz(topic, num_questions, difficulty):
    '''
    Function to generate quiz based on topic, number of questions, and difficulty level

    Args:
        topic (str): The topic for the quiz.
        num_questions (int): The number of questions to generate.
        difficulty (str): The difficulty level of the quiz ("Easy", "Moderate", "Hard").

    Returns:
        response.content (str): The generated quiz content.
    '''
    # Generate the quiz prompt template with dynamic inputs
    prompt_template = prompt.quiz_generator_prompt(topic, num_questions, difficulty)
    # Initialize the language model
    llm = create_chatgroq()

    # Chain the prompt template with the language model
    chain = prompt_template | llm
    
    # Invoke the chain with the relevant parameters
    response = chain.invoke({ 
        "topic": topic,
        "num_questions": num_questions,
        "difficulty": difficulty
    })
    
    return response.content
