num = input("Enter Integer or Float number: ")

try:
    try:
        int(num)
    except ValueError:
        float(num)
    res = 1
except ValueError:
    res = 0

print(res)
