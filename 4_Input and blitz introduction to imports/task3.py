# Words combination
word = input('Enter your word: ')
i = 0
j = 0
while i < len(word):
    new_word = word[i]
    while j < len(word):
        # print(new_word)
        if j != i:
            new_word = new_word + word[j]
            j += 1
        else:
            j += 1
    print(new_word)
    i += 1
    j = 0
