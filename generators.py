from random import choice, randrange
from string import ascii_uppercase


bun_name = ''.join(choice(ascii_uppercase) for b in range(10))
ingredient_name = ''.join(choice(ascii_uppercase) for i in range(10))
bun_price = randrange(100, 1000)
ingredient_price = randrange(100, 1000)
