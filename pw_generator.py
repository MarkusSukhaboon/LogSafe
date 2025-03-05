import random
import string

def create_pw(pw_length):
    """ Get random password of pw_length_var with
    letters, digits, and symbols"""
    characters = string.ascii_letters + string.digits + string.punctuation
    #print(type(characters))
    password = ''.join(random.choice(characters) for i in range(pw_length))
    print("Random password is:", password)
    #return password_var
    return password