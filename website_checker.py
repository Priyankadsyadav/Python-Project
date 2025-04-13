<<<<<<< HEAD
print("Website URL checker")

url=input("Enter a website URL:")

if url.startswith("https://"):
    print("This website is secure")
elif url.startswith("http://"):
    print("Not a secure website")
else:
=======
print("Website URL checker")

url=input("Enter a website URL:")

if url.startswith("https://"):
    print("This website is secure")
elif url.startswith("http://"):
    print("Not a secure website")
else:
>>>>>>> e918ebbfd5dd19b092988c31ccd9400f60cb1272
    print("This does not look like a complete URL")