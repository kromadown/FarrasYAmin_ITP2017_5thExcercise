def log(original_function):
    def new_function(*args, **kwargs):
        with open("log.txt", "w") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))
        return original_function(*args, **kwargs)
    return new_function

@log
def total(x, y):
    return print(x + y)
total(10, 1)

with open("log.txt", "r") as logfile:
    print(logfile.read())
