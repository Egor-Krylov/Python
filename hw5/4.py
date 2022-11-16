inputText = input('Введите текст: ')
previousSymbol = inputText[0]
currentlength = 1
resultText = ''
for i in range(1, len(inputText)):
    if inputText[i] == previousSymbol:
        currentlength += 1
    else:
        resultText += f'{currentlength}{previousSymbol}'
        previousSymbol = inputText[i]
        currentlength = 1

resultText += f'{currentlength}{previousSymbol}'

print(resultText)
