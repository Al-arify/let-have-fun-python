spell = input("Enter string: ").lower()
vowels = consonants = 0
for chr in spell:
    if chr.isalpha():
        if chr in "aeiou":
            vowels += 1
        else:
            consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")