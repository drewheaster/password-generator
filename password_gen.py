import random
import string
import time

new = ''

def get_password(i):
    password = ''
    length = input('How long would you like your password to be? ')
    print('Generating password...')
    time.sleep(3)
    while len(password) <= int(length):
        number = str(random.randint(0,9))
        letter = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        password += number + letter + symbol
    return password

word = get_password(new)
new_word = list(word)
random.shuffle(list(word))
new_password = ''.join(new_word)
print(new_password)