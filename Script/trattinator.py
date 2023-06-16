with open("trattinator.txt", "r") as f:
    content = f.read()
with open("trattinator.txt", "w") as f:
    f.write("- " + content.replace("\n", "\n- "))