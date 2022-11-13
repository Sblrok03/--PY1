import random


def get_random_password(n = 8) -> str:
    from random import sample
    import string
    stroka = string.ascii_lowercase + string.ascii_uppercase + string.digits
    myString = ''.join(random.sample(stroka, n))
    return myString



print(get_random_password())
