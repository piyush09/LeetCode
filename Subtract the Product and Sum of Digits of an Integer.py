def subtractProductAndSum(n):
    prod = 1
    summation = 0

    while n:
        digit = n % 10
        summation += digit
        prod = prod * digit

        n = n // 10

    return (prod - summation)

n = 234

print (subtractProductAndSum(n))
