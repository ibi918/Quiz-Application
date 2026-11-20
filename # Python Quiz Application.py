# Python Quiz Application

# Step 1: Store questions in a list of dictionaries

questions = [
    {
        "question": "What is the capital of India?",
        "options": [
            "A. Delhi",
            "B. Mumbai",
            "C. Kolkata",
            "D. Chennai"
        ],
        "answer": "A"
    },

    {
        "question": "Which language is used for web development?",
        "options": [
            "A. Python",
            "B. Java",
            "C. HTML",
            "D. C++"
        ],
        "answer": "C"
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Computer Personal Unit",
            "C. Central Processing Unit",
            "D. Control Panel Unit"
        ],
        "answer": "C"
    },

    {
        "question": "Which data type stores True or False?",
        "options": [
            "A. Integer",
            "B. String",
            "C. Boolean",
            "D. Float"
        ],
        "answer": "C"
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "A. function",
            "B. def",
            "C. return",
            "D. print"
        ],
        "answer": "B"
    }
]


# Step 2: Initialize score

score = 0

# Calculate total questions
total = len(questions)


# Step 3: Display quiz heading

print("\n========== PYTHON QUIZ ==========")
print("Choose the correct option (A/B/C/D)")
print("=================================")


# Step 4: Display questions using a loop

for i, q in enumerate(questions, 1):

    print(f"\nQ{i}. {q['question']}")

    # Display all options
    for option in q["options"]:
        print(option)

    # Take answer from user
    while True:
        user_ans = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_ans in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C or D.")


    # Step 5: Check answer

    if user_ans == q["answer"]:
        print("Correct!")
        score += 1

    else:
        print(f"Wrong! Correct answer is {q['answer']}")


# Step 6: Calculate final result

percentage = (score / total) * 100


# Step 7: Calculate grade

if percentage >= 80:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "D"


# Step 8: Display final result

print("\n========== QUIZ COMPLETED ==========")

print(f"Your Score: {score} out of {total}")

print(f"Percentage: {percentage:.2f}%")

print(f"Your Grade: {grade}")

print("====================================")