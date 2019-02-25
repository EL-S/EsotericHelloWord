import random
import os

correct_word = "hey"
word_len = len(correct_word)

while True:
    random_seed_value = os.urandom(16)

    random.seed(random_seed_value)

    word = ''.join([chr(random.randint(0, 127)) for i in range(word_len)])

    if word == correct_word:
        break

print(random_seed_value)
print(word)
