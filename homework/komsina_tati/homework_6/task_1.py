text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
fin_words = []
for word in words:
    if word.endswith(','):
        word = word[:-1]
        fin_word = word + 'ing' + ','
        fin_words.append(fin_word)
    elif word.endswith('.'):
        word = word[:-1]
        fin_word = word + 'ing' + '.'
        fin_words.append(fin_word)
    else:
        fin_word = word + 'ing'
        fin_words.append(fin_word)
print(' '.join(fin_words))
