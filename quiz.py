"""
Holton College Digital Quiz System
Student: 2434779
Module: COM4402 - Programming
Description: Console-based quiz application for student assessment
Version 2: Add question display functionality
"""

def initialize_quiz_data():
    # Initialize quiz questions, options, and correct answers using appropriate data structures.
    # Returns: Tuple containing questions list, options list, and answers list
    
    # List of quiz questions (strings)
    questions = [
        "What is the capital of France?",
        "Which programming language is known for its use in data science?",
        "What does CPU stand for?",
        "In Python, which data structure is immutable?",
        "What year was Python first released?"
    ]
    
    # List of lists containing multiple choice options
    options = [
        ["1. London", "2. Berlin", "3. Paris", "4. Madrid"],
        ["1. Java", "2. Python", "3. C++", "4. Ruby"],
        ["1. Central Processing Unit", "2. Computer Personal Unit", "3. Central Program Utility", "4. Computer Processing Utility"],
        ["1. List", "2. Dictionary", "3. Tuple", "4. Set"],
        ["1. 1989", "2. 1991", "3. 1995", "4. 2000"]
    ]
    
    # List storing correct answers (as integers 1-4)
    correct_answers = [3, 2, 1, 3, 2]
    
    return questions, options, correct_answers


def display_question(question_num, question_text, question_options):
    """
    Display a single question with its options.
    
    Args:
        question_num: Current question number
        question_text: The question to display
        question_options: List of multiple choice options
    """
    print(f"\n{'='*60}")
    print(f"Question {question_num}")
    print(f"{'='*60}")
    print(f"\n{question_text}\n")
    
    for option in question_options:
        print(option)
    print()


# Initialize quiz data
questions, options, correct_answers = initialize_quiz_data()
total_questions = len(questions)

print("\n" + "="*60)
print("WELCOME TO HOLTON COLLEGE DIGITAL QUIZ SYSTEM")
print("="*60)

# Display all questions
for index in range(total_questions):
    question_number = index + 1
    display_question(question_number, questions[index], options[index])
