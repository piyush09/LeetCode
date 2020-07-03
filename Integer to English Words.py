oneTo19 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

thousands = ["", "Thousand", "Million", "Billion"]

def check(num):
    if num == 0:
        return ""

    elif (num < 20):
        return oneTo19[num] + " "

    elif (num < 100):
        return tens[num // 10] + " " + check(num % 10)

    else:
        return oneTo19[num // 100] + " Hundred " + check(num % 100)

def numberToWords(num):
    if (num == 0):
        return "Zero"

    result = ""

    for i in range(len(thousands)):

        # Checking the (num % 1000) value, in order to get number of thousands, millions or billions
        if (num % 1000) != 0:
            result = check(num % 1000) + thousands[i] + " " + result

        num = num // 1000

    return result.strip()

num = 1249
print (numberToWords(num))