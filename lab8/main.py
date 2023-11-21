def sum(num):
    summa = 0
    i = len(str(num))
    while i != 0:
        summa += int(num[i-1])
        i -= 1
    return summa

num = input('Enter a number: ')


print(sum(num))