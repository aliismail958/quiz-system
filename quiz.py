"""
Holton College Digital Quiz System
Student: 2434779
Module: COM4402 - Programming
Description: Console-based quiz application for student assessment
Version 1: Basic structure and data initialization
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

# Initialize quiz data
questions, options, correct_answers = initialize_quiz_data()

print("Quiz data initialized successfully!")
print(f"Total questions: {len(questions)}")
