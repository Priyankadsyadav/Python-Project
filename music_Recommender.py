import random

print("Music Recommender")

genres ={
    "rock": ["AC/DC","Queen","Lep Zepplin"],
    "pop": ["Taylor Swift","Ed Sheeran","Ariana Grande"],
    "hip-hop": ["Kendrick Lamar","Drake"]
}

choice = input("What genre would you like? (rock/pop/hip-hop): ")

if choice not in genres:
    print("Sorry,This genre is not available")
else:
    print(f"check out {random.choice(genres[choice])}")