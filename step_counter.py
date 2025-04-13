print("Step counter")

daily_goal=int(input("What is your daily step goal: "))
current_Steps=int(input("Ho many steps have you taken today: "))

remaining_goal = daily_goal-current_Steps

if remaining_goal>0:
    print(f"you need {remaining_goal} more to reach your goal")
else:
    print(f"Congratulations! You've exceeded your goal by {-remaining_goal} steps ")
