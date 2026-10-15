from flask import Flask, render_template, request ,redirect , url_for , flash

app = Flask(__name__)
app.secret_key = 'f02488384727217f065be95be39a4a787e896243a61050f7e1794403e0e4a29c'

USERNAME = 'jamick'
PASSWORD = '12345678'

@app.route('/', methods= ['GET' , 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')
@app.route('/success')
def dashboard():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True , port = 5001)