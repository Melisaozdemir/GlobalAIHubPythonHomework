values = list(range(5))

def valueType(value):
    try:
        if float(value) % 1 == 0:
            return "int"
        else:
            return "float"
    except ValueError:
        return "str"

for i in range(5):
    values[i] = input("Enter the value of your {}" + ". element: ".format(str(i)))

print(values)

forCount = 0
for k in values:
    currentType = valueType(k)
    print(str(forCount) + f". Element = {k}" + f" is a {currentType}")
    forCount += 1