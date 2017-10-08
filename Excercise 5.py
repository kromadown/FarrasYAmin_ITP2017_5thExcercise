import math
def calculator(a, b, operation="plus", output="float"):
    try:
        if operation=="plus":
            result = a + b
        elif operation=="minus":
            result = a - b
        elif operation=="multi":
            result = a * b
        elif operation=="div":
            result = a / b

        if output=="float":
            return result
        elif output=="int":
            return round(result)
    except:
        print ("Error")

print(calculator(2, 3.0))
print(calculator(2, 3.0, output="int"))
print(calculator(2, 3.0, operation="div"))
print(calculator(2, 3.0, operation="div", output="int"))
