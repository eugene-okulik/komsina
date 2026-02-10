words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
counts = []
keys = list(words.keys())
for values_from_words in keys:
    counts.append(words[values_from_words])
for keys_from_words in range(len(keys)):
    print(keys[keys_from_words] * counts[keys_from_words])

