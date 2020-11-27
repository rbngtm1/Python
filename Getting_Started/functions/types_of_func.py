# 1. func that perform a task (eg. func1)
# 2. func that returns a value (eg. round(1.8))

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("robin")
file = open("context.txt", "w")
file.write(message)