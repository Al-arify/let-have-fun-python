total = 0
count = 0
while True:
    num = float(input("Enter number (-1 to stop the running average): "))
    if num == -1:
        break
    total += num
    count += 1
    print("Running Average:", total / count)