# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


# функция которая из строки с многочленом возвращает список коеффициентов многочлена, в том числе нулевые коеффициенты
def GetPower(elementString): 
    if ('^' in elementString):
        return int(elementString.split('^')[1])
    elif ('x' in elementString):
        return 1
    else:
        return 0


def GetCoef(elementString):
    if ('x' in elementString):
        if ('*' in elementString):
            return float(elementString.split("*")[0])
        else:
            return 1.0
    else:
        return float(elementString)

def GetCoefs(polynomString):
    polynomSplitted = polynomString.split(' + ')
    result = [0 for i in range(GetPower(polynomSplitted[0]) + 1)]
    for i in polynomSplitted:
        result[GetPower(i)] = GetCoef(i)
    return result

def GetPolynomStringByCoefs(coefs):
    resultString = f'{coefs[0]}'
    for i in range(1, len(coefs)):
        element = ''
        if (coefs[i] != 1) and (coefs[i] != 0):
            element = f"{coefs[i]}*x"
        elif coefs[i] == 1:
            element = "x"

        if i > 1 and element != '':
            element += f"^{i}"
            
        if element != '':
            element += " + "

        resultString = element + resultString
    return resultString

# print(GetPolynomStringByCoefs([1,3,6,0,1,4,6,2]))

f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')
coefs1 = GetCoefs(f1.read())
print(coefs1)
coefs2 = GetCoefs(f2.read())
print(coefs2)
resultCoefs = []
for i in range(max(len(coefs1), len(coefs1))):
    coef = 0
    if i < len(coefs1):
        coef += coefs1[i]
    if i < len(coefs2):
        coef += coefs2[i]
    if coef % 1 == 0:
        coef = round(coef)
    resultCoefs.append(coef)

print(GetPolynomStringByCoefs(resultCoefs))
f1.close()
f2.close()