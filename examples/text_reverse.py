with open("lorenipsum.txt", "r") as f:
    content = f.read()

tokens = content.split(' ')
tokens.reverse()
content = " ".join(tokens)


with open("reverse.txt", "w") as f:
    f.write(content)
