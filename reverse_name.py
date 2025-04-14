print("REVSERSE NAME GENERATOR")

while True:
    name=input("Enter the name: ")

    if not name:
        break

    reversed_name = name[::-1]
    print(f"Your reversed name is: {reversed_name}")
    print(f"In paralled universe, they call you {reversed_name.title()}")

    answer = input("\n Try another name? (Yes/No): ")

    if answer not in  ["yes","Y","y"]:
        break