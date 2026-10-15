from flask import Flask, render_template, request ,redirect , url_for , flash

app = Flask(__name__)
app.secret_key = ''

USERNAME = 'jamick'
PASSWORD = '12345678'

@app.route('/', methods= ['GET , POST'])
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
@app.route('/succcess')
def dashboard():
    return render_template('succeess.html')

if __name__ == '__main__':
    app.run(debug=True)