import math
def calculator(operation="plus", output="float", *numbers):
    try:
        total = 0
        spec = ""
        final = 0
        if operation=="plus":
            for number in numbers:
                total += number
            final = total
        elif operation=="minus":
            for number in numbers:
                total -= number
            final = total
        elif operation=="multi":
            for number in numbers:
                multiply = number
                if spec == "":
                    spec = number
                else:
                    spec = spec*multiply
            final = spec
        elif operation=="div":
            for number in numbers:
                divide = number
                if spec == "":
                    spec = number
                else:
                    spec = spec/divide
            final = spec

        if output=="float":
            return final
        elif output=="int":
            return round(final)
    except TypeError:
        print ("Error")

print(calculator("multi", "int", 6, 4, 9, 1))
