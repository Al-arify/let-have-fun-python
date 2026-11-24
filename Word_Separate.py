spell = input("Enter sentence: ")
word = ""
for chr in spell + " ":
    if chr == " ":
        if word != "":
            print(word)
            word = ""
    else:
        word += chr