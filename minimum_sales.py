target = 30000
sales = 0
while True:
    sales += 1
    if sales <= 5000:
        comm = sales * 0.06
    elif sales <= 10000:
        comm = 300 + (sales - 5000) * 0.08
    else:
        comm = 700 + (sales - 10000) * 0.10
    if comm >= target:
        break
print("Minimum sales:", sales)