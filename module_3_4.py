def single_root_words(root_word, *other_words):
    same_words = []
    for key in other_words:
        a = key.lower()
        b = root_word.lower()
        if b in a:
            same_words.append(key)
        if a in b:
            same_words.append(key)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
