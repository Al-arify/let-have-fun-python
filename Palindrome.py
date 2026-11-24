spell = input("Enter string: ").lower().replace(" ", "")
reversed_spl = ""
for ch in spell:
    reversed_spl = ch + reversed_spl
print("Palindrome" if spell == reversed_spl else "Not Palindrome")