# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

inputText = input('Введите текст: ')

words = inputText.split(' ')
wordsResult = []
for i in words:
    if not "абв" in i:
        wordsResult.append(i)
print(' '.join(wordsResult))