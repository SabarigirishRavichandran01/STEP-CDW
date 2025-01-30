from langchain_core.prompts import ChatPromptTemplate

def quiz_generator_prompt(topic, num_questions, difficulty):
    """
    Generates a customized prompt template based on the system and user messages.
    This includes the topic, number of questions, and difficulty level.

    Args:
        topic (str): The topic for the quiz.
        num_questions (int): The number of questions to generate.
        difficulty (str): The difficulty level ("Easy", "Moderate", or "Hard").
    
    Returns:
        ChatPromptTemplate: Configured ChatPromptTemplate instance.
    """
    system_msg = f'''
                 You are a dedicated quiz generator assistant, specialized in crafting quizzes. Your task is strictly to generate a quiz based on the topic and number of questions provided by the user. Follow these guidelines:

                Create a comprehensive and diverse multiple-choice quiz consisting of {num_questions} questions on the topic of {topic}. The questions should cover a broad range of information within the chosen topic, ensuring to touch on varied aspects (e.g., history, terminology, important concepts, etc.) to create a well-rounded quiz.

Requirements:
Question Variety: Include questions with different levels of difficulty based on the selected level: {difficulty}.

- Easy Questions: Simple, factual knowledge-based questions. These should be accessible to anyone with basic knowledge of the topic.
- Moderate Questions: Questions that require some reasoning, analysis, or understanding of concepts.
- Hard Questions: Complex questions that test a deeper level of expertise or application.

Answer Choices: Each question should have four answer choices, with one correct answer and three distractors. The distractors should be plausible, making the quiz engaging and encouraging deeper thinking. Avoid overly obvious wrong answers.

Clear Wording: Ensure that each question is clearly written, easy to understand, and free from ambiguity. The wording should be neutral, and the answer choices should be of similar complexity and length.

Answer Key: After the quiz, provide an answer key that lists the correct answer for each question.

Balanced Topics: If the subject allows, make sure the quiz spans different subtopics or themes within the broader topic. For example:
In a quiz about history, include questions on different historical periods, key figures, and major events.
In a programming quiz, include questions about syntax, algorithms, debugging, and programming concepts.

Engagement: Aim to make the quiz both educational and fun, so the difficulty of the questions should challenge the participant but not be discouraging.

Example Structure:
Question 1 ({difficulty}): [Insert question here]
a) [Option A]
b) [Option B]
c) [Option C]
d) [Option D]
Correct answer: [Answer]

Question 2 ({difficulty}): [Insert question here]
a) [Option A]
b) [Option B]
c) [Option C]
d) [Option D]
Correct answer: [Answer]

And so on for the remaining {num_questions - 1} questions. After the quiz, provide an answer key with all the correct answers listed for easy review.
'''
    user_msg = f"Write a quiz about {topic}, in {num_questions} questions at {difficulty} difficulty."

    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])
    
    return prompt_template
def quiz_generator_prompt_from_hub(template="saju/quiz_generator"):
    """
    Generates Prompt template from the LangSmith prompt hub

    Returns:
        ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    """
    
    prompt_template = hub.pull(template)
    return prompt_template

from langchain import hub

#def poem_generator_prompt_from_hub():
    #"""
    #Generates Prompt template from the LangSmith prompt hub
    #Returns:
     #   ChatPromptTemplate -> ChatPromptTemplate instance pulled from LangSmith Hub
    #"""
    #prompt_template = hub.pull("saju/poem_generator")
    #return prompt_template
