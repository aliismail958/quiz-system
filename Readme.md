# Holton College Digital Quiz System

**Student Number:** 2434779  
**Module Code:** COM4402  
**Module Name:** Programming  
**Assignment:** Part 2 - Implementation (70% of Portfolio Component)

## Project Description

This is a console-based quiz application developed in Python as a Proof of Concept for Holton College's digital assessment system. The application presents students with multiple-choice questions, validates their answers, tracks their score, and provides performance feedback.

## Features

- **5 Multiple Choice Questions** covering various topics
- **Input Validation** to ensure users enter valid responses
- **Real-time Feedback** after each question
- **Score Tracking** throughout the quiz
- **Performance Feedback** based on final percentage
- **Clean, Modular Code** following PEP 8 guidelines

## Technical Details

### Data Structures Used

- **Lists** - Store questions, options, and correct answers
- **Tuples** - Return multiple values from initialization function
- **Integers** - Track score and question indices
- **Strings** - Store question text and display messages

### Functions

- `initialize_quiz_data()` - Sets up quiz questions and answers
- `display_question()` - Presents questions to the user
- `get_user_answer()` - Handles and validates user input
- `check_answer()` - Compares user answer with correct answer
- `display_results()` - Shows final score and feedback
- `run_quiz()` - Main program coordinator

## How to Run the Program

### Prerequisites

- Python 3.x must be installed on your system
- No additional libraries required (uses only Python standard library)

### Running the Quiz

1. Clone this repository or download the `quiz.py` file
2. Open a terminal/command prompt
3. Navigate to the directory containing `quiz.py`
4. Run the following command:

```bash
python quiz.py
```

or on some systems:

```bash
python3 quiz.py
```

5. Follow the on-screen instructions
6. Enter your answers using numbers 1-4
7. View your final score at the end

## Development Process

This project was developed following a structured approach:

1. **Planning** - Created flowchart and pseudocode
2. **Implementation** - Built modular functions in Python
3. **Testing** - Validated with various input scenarios
4. **Version Control** - Regular commits documenting progress

## Testing

The application has been thoroughly tested with:
- Valid inputs (numbers 1-4)
- Invalid inputs (letters, symbols, out-of-range numbers)
- Boundary cases
- All correct answers scenario
- All incorrect answers scenario

See the full report for detailed test cases and results.

## File Structure

```
quiz-system/
│
├── quiz.py          # Main quiz application
└── README.md        # This file
```

## License

This project is submitted as coursework for COM4402 Programming module at Holton College.

## Contact

Student Number: 2434779  
Module: COM4402 - Programming
