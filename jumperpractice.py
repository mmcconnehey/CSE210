import random
word_list = ['yes']
user_word = []

word = random.choice(word_list)
print(word)
for letter in word:
    i = letter

guess = input('A-Z ')

while guess != i:
    guess = input('a-z ')