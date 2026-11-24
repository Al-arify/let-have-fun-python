def my_length(word):
    count = 0
    for letter in word:
        count += 1
    return count

print(my_length("eggroll"))