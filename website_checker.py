print("Website URL checker")

url=input("Enter a website URL:")

if url.startswith("https://"):
    print("This website is secure")
elif url.startswith("http://"):
    print("Not a secure website")
else:
    print("This does not look like a complete URL")