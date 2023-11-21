def sum(num:str) -> int: 
    summa = 0
    i = len(str(num))
    while i != 0:
        summa += int(num[i-1])
        i -= 1
    return summa
try:
    num = input('Enter a number: ')
    if num.isdigit():
        print(sum(num))
    else:
        print("Please enter digits only")
except ValueError:
    print("Invalid input")


# def check_float(number:float) -> bool:
#     try: 
#         float(number)
#         return True
#     except ValueError:
#         return False
    

# def index_mass(mass:float, height:int) -> float:
#     bmi = mass/(height**2)
#     return index_mass_class(bmi)


# def index_mass_class(bmi:float) -> str:
#     if bmi <= 18.5:
#         return "You are thin"
#     elif 18.5 < bmi <= 25:
#         return "You have normal weight"
#     elif 25 < bmi <= 30:
#         return "You are overweight"
#     else:
#         return "You are obese"

# try:
#     mass = input("Enter your mass: ")
#     height = input("Enter your height: ")
#     if check_float(mass) and height.isdigit():
#         print(index_mass(float(mass), int(height)))
#     else:
#         print("Please enter digits only")
# except ValueError:
#     print("Invalid input")

















