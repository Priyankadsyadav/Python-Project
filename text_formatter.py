print("TEXT CAPITALIZER")

text=input("Enter some text: ")

print("1. Lower case")
print("2. Upper case")
print("3. Title case")
print("4. Sentence case")

choice=input("Choose the format (1-4): ")

if choice == "1":
    print(text.lower())
elif choice == "2":
    print(text.upper())
elif choice == "3":
    print(text.title())
elif choice == "4":
    print(text.capitalize())