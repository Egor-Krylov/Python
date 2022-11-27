# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Старый код:

# inputText = input('Введите текст: ')

# words = inputText.split(' ')
# wordsResult = []
# for i in words:
#     if not "абв" in i:
#         wordsResult.append(i)
# print(' '.join(wordsResult))

# Новый код:

words = input('Введите текст: ').split(' ')

print(' '.join(filter(lambda word: not "абв" in word, words)))
