#Quiz Game:

Questions=[
    {
        "prompt":"What is the capital of france?",
         "options":["A. Paris","B. London","C. Berlin","D. Madrid"],
         "Answer": "A"},

         {"prompt":"What is language of spain ?",
         "options":["A. German","B. Polish","C. Spanish","D. Ukranish"],
         "Answer": "C"},

         {"prompt":"What is the whole number?",
         "options":["A. 9","B. 2","C. 1","D. 0"],
         "Answer": "D"},

         {"prompt":"What is the smallest prime number?",
         "options":["A. 2","B. 10","C. 1","D. -1"],
         "Answer": "A"}
]

def run_quiz(Questions):
    score=0      
    for question in Questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer =input("Enter you answer (A/B/C/D):").upper()
        if answer==question["Answer"]:
            print("Correct answer \n")
            score+=1
        else:
            print("You are wrong here. \n The correct answer was => ",question["Answer"])

    print(f"Your score : {score} out of {len(Questions)}")

run_quiz(Questions) 