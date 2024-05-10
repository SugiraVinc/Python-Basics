# a function that checks validity of a username
def hit_usernamet(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Your name is valid")
name = input("please enter your name: ")
hit_usernamet(name)