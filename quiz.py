"""
Holton College Digital Quiz System
Student: 2434779
Module: COM4402 - Programming
Description: Console-based quiz application for student assessment
Version 6: Improve user experience with pause prompts
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


def get_user_answer():
    """
    Prompt user for their answer and validate input.
    Returns: Integer representing user's choice (1-4)
    """
    while True:
        try:
            user_input = input("Enter your answer (1, 2, 3, or 4): ").strip()
            answer = int(user_input)
            
            if 1 <= answer <= 4:
                return answer
            else:
                print("Invalid input! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")


def check_answer(user_answer, correct_answer):
    """
    Compare user's answer with correct answer.
    
    Args:
        user_answer: The user's selected answer
        correct_answer: The correct answer
    
    Returns: Boolean - True if correct, False otherwise
    """
    return user_answer == correct_answer


def display_results(score, total_questions):
    """
    Display final quiz results with score and percentage.
    
    Args:
        score: Number of correct answers
        total_questions: Total number of questions in quiz
    """
    percentage = (score / total_questions) * 100
    
    print(f"\n{'='*60}")
    print("QUIZ COMPLETED")
    print(f"{'='*60}")
    print(f"\nYour final score: {score} out of {total_questions}")
    print(f"Percentage: {percentage:.1f}%")
    
    # Provide feedback based on performance
    if percentage >= 80:
        print("\nExcellent work! Outstanding performance!")
    elif percentage >= 60:
        print("\nGood job! You passed the quiz.")
    elif percentage >= 40:
        print("\nNot bad, but there's room for improvement.")
    else:
        print("\nKeep practicing! You'll do better next time.")
    
    print(f"\n{'='*60}\n")


def run_quiz():
    """
    Main function to execute the quiz program.
    Coordinates all quiz operations from start to finish.
    """
    # Display welcome message
    print("\n" + "="*60)
    print("WELCOME TO HOLTON COLLEGE DIGITAL QUIZ SYSTEM")
    print("="*60)
    print("\nThis quiz contains 5 multiple choice questions.")
    print("Answer each question by entering the number (1-4) of your choice.")
    print("\nGood luck!\n")
    input("Press Enter to start the quiz...")
    
    # Initialize quiz data
    questions, options, correct_answers = initialize_quiz_data()
    total_questions = len(questions)
    score = 0
    
    # Loop through each question
    for index in range(total_questions):
        question_number = index + 1
        
        # Display current question
        display_question(question_number, questions[index], options[index])
        
        # Get user's answer
        user_answer = get_user_answer()
        
        # Check if answer is correct
        if check_answer(user_answer, correct_answers[index]):
            print("\n✓ Correct!")
            score += 1
        else:
            print(f"\n✗ Incorrect. The correct answer was: {correct_answers[index]}")
        
        # Brief pause before next question
        if index < total_questions - 1:
            input("\nPress Enter to continue to the next question...")
    
    # Display final results
    display_results(score, total_questions)


# Main program entry point
if __name__ == "__main__":
    run_quiz()
