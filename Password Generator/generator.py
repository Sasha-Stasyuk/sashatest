import random 
def generate_password (lowercase, numbers, symbols, uppercase):
    passwords = []
    if lowercase:
        for i in range(4):   
            passwords.append(random.choice("abcdefghikklmnopqrstuvwxyz"))
    if numbers:
        for i in range(4):   
            passwords.append(random.choice("0123456789"))
    if symbols:
        for i in range(4):   
            passwords.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if uppercase:
        for i in range(4):   
            passwords.append(random.choice("!@#$%^&*()"))    
    random.shuffle(passwords)
    return "".join(passwords)
