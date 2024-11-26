from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols):
    character_pool = ''
    
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return None

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_lowercase = 'lowercase' in request.form
        use_uppercase = 'uppercase' in request.form
        use_numbers = 'numbers' in request.form
        use_symbols = 'symbols' in request.form

        generated_password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols)

    return render_template('index.html', password=generated_password)

if __name__ == '__main__':
    app.run(debug=True)