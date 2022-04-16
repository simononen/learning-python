from argon2 import hash_password


username = input('Enter username? ')
password = input('Enter your password? ')

password_length = len(password)
hash_password = '*' * password_length

print(f'{username}, your password {hash_password} is {password_length} characters long.')
