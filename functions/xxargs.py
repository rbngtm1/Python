# passing keyword-argument to function
def save_user(**user):
    print(user["name"])


save_user(id=3, name="Jackson", age=22)