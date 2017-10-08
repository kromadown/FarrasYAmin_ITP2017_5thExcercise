def factorial(num):
    try:
        if num == 1:
            return 1
        else:
            return (num*factorial(num-1))
    except:
        if num < 0:
            return None

print(factorial(int(input())))
