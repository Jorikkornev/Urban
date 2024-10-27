def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()

    for word in other_words:
        word = word.lower()
        if word.count(root_word):
            same_words.append(word)
        elif len(word) >= 3 and len(root_word) >= len(word) and  root_word.find(word) != -1:
            same_words.append(word)
            #  print('Root_word: ', root_word, 'Word: ', word)
    return same_words

# Вызов функции и вывод результата
result = single_root_words("root", "roOt1", "Rootto", "Ortoroot", "ro0t4", 'roo', 'otto')
print(result)
