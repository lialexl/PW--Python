# def greet():
#     print("Hello")
# greet()


# def greet_name(name):
#     print(f"Hello {name}")
# greet_name("Alex")


# def max_min(num1, num2, num3):
#     max_num = max(num1, num2, num3)
#     min_num = min(num1, num2, num3)
#     return min_num, max_num 

# print(max_min(50, 20, 30))

# def word_len(word):
#     return len(word)
# print(word_len("Python123"))

# def silnia(num):
#     if num == 0:
#         return 1
#     else:
#         return num * silnia(num-1)

# print(silnia(5))

# def sum(num1: int, num2: int) -> int:
#     return num1 + num2
# print(sum(1, 2))

#import requests as rq

# responce = rq.get('https://www.google.com')
# print(responce.text)
# print(responce.status_code)

# e_mail = input("Input your e-mail: ")
# if e_mail.count('@') == 1:
#        pass
# elif 6 < len(e_mail) < 30:
#     pass
# elif  ";" in e_mail or   ":" in e_mail or  "-" in e_mail or  " " in e_mail:
#     pass
# elif "pw.edu.pl" in e_mail:
#     print("Your e-mail is valid")
# else:
#     print("Your e-mail is not valid")
        

# def validate_email(email):
#     if email.count("@") != 1:
#         raise ValueError('This is not a valid e-mail')
    
#     param = email.split("@")
#     if param[1] == 'pw.edu.pl':
#         raise ValueError('The domain is not of pw.edu.pl')

#     return True

    
# try:
#     validate_email('askdlk@pw.edu.pl')
# except ValueError as e:
#     print(f"Error code: {e}")


# def validate_password(password):

#     is_upper = any(char.isupper() for char in password)
#     is_digit = any(char.isdigit() for char in password)
#     is_long = len(password) >= 8
#     return is_upper and is_digit and is_long

# passw = input("Enter your password: ")

# if validate_password(passw):
#     print("This is a strong password")
# else: 
#     print("This is a weak password")


# def validate_username(username):
#     return username.isalnum() and 3 <= len(username) <= 16

# user = input("Enter a username: ")
# if validate_username(user):
#     print("You entered a correct username")
# else:
#     print("The username is not correct")


# def validate_ip(ipnet):
#     param = ipnet.split('.')
#     if len(param) != 4:
#         return False
#     for part in param:
#         if not part.isdigit() or not 0 <= int(part) <= 255:
#             return False
#     return True


# print(validate_ip('192.160.5.1'))



# def validate_nip(nip):
#     if not nip.isdigit() or len(nip) != 10:
#         return False
#     waga = [6, 5, 7, 2, 3, 4, 5, 6, 7]

#     suma = 0
#     for i in range(9):
#         suma += int(nip[i]) * waga[i]
#     if suma % 11 != int(nip[9]):
#         return False
    
#     return True

# print(validate_nip('1234563218'))












