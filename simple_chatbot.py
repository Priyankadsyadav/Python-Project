import random
import time

def chatbot():
    greetings=["Hello","Hi","Nice to meet you","Hi Friend","How are you doing today"]

    farewells=["Goodbye","Bye, until next time","Bye","bye","Ciao","See you soon"]

    jokes = [
        "Why do programmers prefer dark mode?- Because the light attracts bugs.",
        "How many programmers does it take to change a light bulb? - None, that’s a hardware problem.",
        "I told my computer I needed a break... - Now it won’t stop sending me Kit-Kat ads.",
        "Why can't you trust an atom? - Because they make up everything!",
        "What’s a physicist’s favorite food? - Fission chips.",
        "Why did the function break up with the loop? : It got stuck in a never-ending relationship.",
        "What do you call fake spaghetti? - An impasta.",
        "Why don’t skeletons fight each other? - They don’t have the guts."
    ]

    facts = [
        "You’re taller in the morning than in the evening — gravity compresses your spine throughout the day",
        "Your brain uses about 20% of your body’s total energy",
        "Humans glow in the dark — but the light is 1,000 times weaker than our eyes can detect",
        "The average person walks the equivalent of 5 times around the world in a lifetime.",
        "A day on Venus is longer than a year on Venus",
        "The first email ever sent was “QWERTYUIOP”.",
        "The first webcam was used to monitor a coffee pot at Cambridge University."
    ]

    bot_name="Chatbot"
    print(f"{bot_name} is starting up ....")
    time.sleep(1)

    print(f"""
            Welcome to {bot_name}!
            I can chat about :
            'Joke' - hear a funny joke
            'fact' - Learn something new
            'color' - My favorite color
            'bye' - End our chat

            """)
    
    chatting = True

    user_name = input("Enter you name:  ".lower().strip())
    print(f"{bot_name}:Nice to meet you, {user_name} ! How can I help you ?")    

    while chatting:
        user_input= input("You: ").strip()

        if user_input in ["Hello","Hi","Nice to meet you","Hi Friend","How are you doing today"]:
            print(f"{bot_name}: {random.choice(greetings)}")
        elif "joke" in user_input:
            print(f"{bot_name}: {random.choice(jokes)}")
        elif "fact" in user_input:
            print(f"{bot_name}: {random.choice(facts)}")
        elif "color" in user_input:
            print(f"{bot_name}: My favorite color is blue. What is your?")
            color= input("You: ").strip()
            print(f"{bot_name}: {color} is a great color")
        elif user_input in ["Goodbye","Bye, until next time","Bye","Ciao","See you soon"]:
            print(f"{bot_name}: {random.choice(farewells)}")
            print(f"{bot_name}: It was fun chatting with you {user_name}")
            chatting =False
        else:
            responses=[
                "That's interesting, tell me more",
                "I am sure, if I understand you",
                "Beep Beep! My robot brain is processing that.."
            ]
            print(f"{bot_name}: {random.choice(responses)}")
    print("Thanks for chatting. \n Run the Program to run again")
chatbot()