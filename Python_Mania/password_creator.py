import random
import math
import gradio as gr

alpha = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
spl_char = '!@#$%^&*()'

password_length = int(input("Enter the desired password length: "))

alpha_len = math.floor(password_length * 0.40)
num_len = math.floor(password_length * 0.30)
spl_char_len = password_length - (alpha_len + num_len)

password = []

def generate_password(alpha_len, num_len, spl_char_len):
    for i in range(alpha_len):
        char = random.randint(0,1)
        if char == 1:
            password.append(random.choice(alpha.upper()))
        else:
            password.append(random.choice(alpha))
        
    num_vals = random.sample(num, num_len)
    password.extend(val for val in num_vals)
    
    spl_characters = random.sample(spl_char, spl_char_len)
    password.extend(char for char in spl_characters)

generate_password(alpha_len, num_len, spl_char_len)
random.shuffle(password)

final_password = ""
for i in password:
    final_password = final_password + str(i)
print(f'Here\'s your password: {final_password}')