def maximum69Number(num):

    stringNumber = str(num)
    for i in range(len(stringNumber)):

        if (stringNumber[i] == '6'):
            stringNumber = stringNumber[:i] + '9' + stringNumber[(i+1):]
            return stringNumber

    return stringNumber
num = 9669
print (maximum69Number(num))