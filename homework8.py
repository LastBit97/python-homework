with open("hello.txt", "r") as file:
    content = file.read()
    reversed_content = ''.join(reversed(content))
    print(reversed_content)
with open("reversed_hello.txt", "w") as newfile:
    newfile.write(reversed_content)
