spell = input("Enter string: ")
rev = ""
for chr in spell:
    rev = chr + rev
print(rev)