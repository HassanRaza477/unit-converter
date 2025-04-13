import hashlib

def generate_password_hash(password):
        return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    'ali@gmail.com': generate_password_hash('password123'),
    'zainab@gmail.com': generate_password_hash('qwertyuiop'),  
    'Hasan@gmail.com': generate_password_hash('letmein'),        
}

def check_password(email, password):
    if email not in stored_logins:
        return False
    stored_hash = stored_logins[email]
    input_hash = generate_password_hash(password)
       
        