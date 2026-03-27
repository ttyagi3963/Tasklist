import json
from pathlib import Path


questions = json.loads(Path('files/questions.json').read_text())
score = 0


for question in questions:
    print(question['question_text'])
    options = question['alternatives']
    for i, option in enumerate(options):
        print(f"{i+1} - {option}")

    user_choice = int(input("Enter your choice: ").strip())
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score = score+1
        print("CORRECT ANSWER \n")
    else:
        print("WRONG ANSWER \n")


print(f"total score {score}/{len(questions)}")





